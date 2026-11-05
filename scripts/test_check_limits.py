import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("check_limits.py")


class CheckLimits(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def write(self, relative_path, line_count):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("line\n" * line_count)

    def run_check(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(self.root), *args],
            capture_output=True,
            text=True,
        )

    def test_files_at_the_limit_pass(self):
        self.write("CLAUDE.md", 80)
        self.write(".claude/skills/a/SKILL.md", 40)
        self.assertEqual(self.run_check().returncode, 0)

    def test_claude_md_over_the_limit_fails_and_names_the_file(self):
        self.write("packages/api/CLAUDE.md", 81)
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("packages/api/CLAUDE.md", result.stdout)

    def test_skill_inside_hidden_folder_is_found(self):
        self.write(".claude/skills/a/SKILL.md", 41)
        self.assertEqual(self.run_check().returncode, 1)

    def test_skill_limit_can_be_changed(self):
        self.write(".claude/skills/a/SKILL.md", 41)
        self.assertEqual(self.run_check("--skill-limit", "41").returncode, 0)

    def test_topic_files_have_no_limit(self):
        self.write(".claude/skills/a/topic.md", 500)
        self.assertEqual(self.run_check().returncode, 0)

    def test_dependency_folders_are_skipped(self):
        self.write("node_modules/pkg/CLAUDE.md", 500)
        self.assertEqual(self.run_check().returncode, 0)

    def test_missing_folder_is_an_error_not_a_pass(self):
        self.root = self.root / "does-not-exist"
        self.assertNotEqual(self.run_check().returncode, 0)


if __name__ == "__main__":
    unittest.main()
