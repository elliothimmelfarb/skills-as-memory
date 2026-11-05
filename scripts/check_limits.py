#!/usr/bin/env python3
"""Fail if any SKILL.md or CLAUDE.md under a folder is over its line limit."""
import argparse
import os
import sys
from pathlib import Path

CLAUDE_MD_LIMIT = 80
DEFAULT_SKILL_LIMIT = 40
SKIPPED_FOLDERS = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def find_violations(root, skill_limit):
    limits = {"CLAUDE.md": CLAUDE_MD_LIMIT, "SKILL.md": skill_limit}
    violations = []
    for folder, subfolders, files in os.walk(root):
        subfolders[:] = [name for name in subfolders if name not in SKIPPED_FOLDERS]
        for name in sorted(set(files) & set(limits)):
            path = Path(folder) / name
            lines = len(path.read_text(errors="replace").splitlines())
            if lines > limits[name]:
                violations.append((path.relative_to(root), lines, limits[name]))
    return sorted(violations)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", type=Path)
    parser.add_argument("--skill-limit", type=int, default=DEFAULT_SKILL_LIMIT)
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error(f"not a folder: {args.root}")

    violations = find_violations(args.root, args.skill_limit)
    for path, lines, limit in violations:
        print(f"{path.as_posix()}: {lines} lines, limit {limit}")
    if violations:
        return 1
    print("All files are within their limits.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
