# skills-as-memory

A template and short guide for storing what a coding agent learns as skills instead of a memory file.

## The problem with memory files

A memory file is one document that the agent reads at the start of every session and adds to as it learns. That works well for a few weeks, and then four problems show up.

- Every line costs context in every session, including sessions that have nothing to do with that line.
- The file only grows, because adding a line is easy and nothing asks anyone to remove one.
- Wrong facts stay in, and the agent trusts them, because a stale line looks the same as a correct one.
- Facts end up in the order they were learned rather than by subject, so a deploy note and its correction can sit a hundred lines apart.

## The rule

Keep what the agent learns in skills, and load it only when the work needs it. A skill is a folder with a `SKILL.md` file. The agent sees each skill's one-line description in every session, and it opens the skill only when the work touches that area.

| When it loads | What loads | Size |
|---|---|---|
| Every session | Project `CLAUDE.md` | 80 lines at most |
| Every session | Each skill's description | One or two sentences |
| Working in that area | `SKILL.md` | A short index, around 25 lines |
| When the detail is needed | Topic files | As long as they need to be |

Four working rules make this hold up over time.

1. **SKILL.md is a short index.** It says what the area covers and points at topic files, and the topic files hold the detail.
2. **The project CLAUDE.md stays short.** It holds only what every session needs, which usually means the commands, the rules that prevent real damage, and these rules.
3. **Read before, write after.** Before working in an area, the agent reads its skill. When it figures out something that was not obvious, it adds that to the skill where it belongs.
4. **Fix stale facts on sight.** If the agent notices that a skill or CLAUDE.md is wrong, it fixes the fact right then. This replaces scheduled cleanups, because the fix happens at the moment someone has the correct information.

## When to create a skill and when to add to one

Add to an existing skill by default, and make a new one only when nothing fits. Too many small skills bring back the original problem, because every description loads in every session.

| What you learned | Where it goes |
|---|---|
| Something about an area that has a skill | That skill's closest topic file |
| A new subject inside an area that has a skill | A new topic file, plus one line in `SKILL.md` |
| An area with no skill that the work will return to | A new skill |
| A rule every session needs, whatever the task | `CLAUDE.md`, if it earns its line |
| Something about you, or something that applies across projects | A skill in `~/.claude/skills/` |
| Something the code or the docs already say | Nowhere. Link to it if it is hard to find |
| The current state of a task | Your issue tracker or a status file, not a skill |

The description matters more than anything else in a skill. It is the only part the agent sees before deciding whether to open the skill, so name the situations that should trigger it.

## Before and after

Before, one memory file holds everything and loads in every session:

```markdown
# Memory

- Use pnpm, not npm.
- 2026-03-02: staging deploy failed, had to clear the build cache.
- The billing webhook secret is different in staging.
- Tests need the database running.
- 2026-04-11: deploys now go through the new pipeline. Ignore the old script.
- Run the old deploy script from the repo root.
- Invoices are rounded per line, not per total.
- 2026-05-20: the build cache problem is fixed upstream.
```

Eight lines in, the file already contradicts itself. The agent cannot tell whether the deploy script is current, or whether the build cache note still matters. A session that only touches invoices loads all of it anyway.

After, the same facts sit where they are used. The stale lines are gone, and a session about invoices loads the short CLAUDE.md and the billing skill, and nothing about deploys.

```text
CLAUDE.md                       Use pnpm. Tests need the database running.
.claude/skills/
  deploys/
    SKILL.md                    Index, with a description naming deploys
    pipeline.md                 How the new pipeline works
  billing/
    SKILL.md                    Index, with a description naming invoices
    invoices.md                 Rounding is per line, not per total
    webhooks.md                 The staging secret is different
```

In the migration this guide came from, six projects moved to this pattern. The longest CLAUDE.md went from 151 lines to 63, and every CLAUDE.md ended up under 80 lines.

## What is here

- `template/`: a CLAUDE.md stub and one example skill, with a `SKILL.md` and two topic files.
- `examples/steam-game/`: a worked example for a fictional studio that ships games to Steam. The `tools/release` commands in it show the shape of real notes, and that tool does not exist in this repo.
- `scripts/check_limits.py`: fails if a `CLAUDE.md` is over 80 lines or a `SKILL.md` is over the limit.

## Using it

Copy the template into your repo, then replace the example skill with one for an area you actually work in.

```sh
cp -R template/. /path/to/your/repo/
```

Turn off automatic memory so the agent has one place to write. In Claude Code, set `"autoMemoryEnabled": false` in `settings.json`. If you already have a memory file, sort each line using the table above, and delete what no longer holds.

The layout here is the one Claude Code uses. Another agent can follow the same files if its instructions tell it to read them, although it may not load skill descriptions on its own.

## Checking the limits

```sh
python3 scripts/check_limits.py /path/to/your/repo
python3 scripts/check_limits.py /path/to/your/repo --skill-limit 30
```

The script needs Python 3 and nothing else. The default limit for `SKILL.md` is 40 lines, which leaves some room above the 25 a skill should aim for. It exits with 1 and names each file that is over, so it works in a pre-commit hook or CI. It checks length only, so it cannot tell you whether a fact is true.

To run its test:

```sh
python3 -m unittest scripts/test_check_limits.py
```

## License

MIT. See `LICENSE`.
