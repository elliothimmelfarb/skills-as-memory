# skills-as-memory

A template and short guide for storing what a coding agent learns as skills instead of a memory file. There is no application here, only documents and one small check script.

## Layout

- `README.md`: the guide.
- `template/`: what people copy into their own repo.
- `examples/steam-game/`: a worked example for a fictional studio.
- `scripts/`: the line limit check and its test.

## Commands

- `python3 -m unittest scripts/test_check_limits.py`: run the test.
- `python3 scripts/check_limits.py .`: check every SKILL.md and CLAUDE.md in the repo.

Run both before committing. The script uses only the Python standard library, and it should stay that way.

## Rules for changing this repo

- Follow the pattern the guide describes. If an edit needs a new rule, put it in the file where it is used.
- The README uses plain sentences, with no em dashes and no slogans.
- Examples stay fictional: no real people, clients, accounts, app IDs or personal paths.
- Do not paste text from other people's skills. Write it fresh.
