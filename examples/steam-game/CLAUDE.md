# Example Studio games

Where a fictional studio makes Godot games and ships them to Steam. Each game is a Godot project in `games/<slug>/`, and `tools/release` is the command line tool that builds and uploads them.

## Commands

- `tools/release doctor`: check the toolchain and the cached build login.
- `tools/release export games/<slug>`: make release builds for each platform.
- `tools/release assets games/<slug>`: check store art against the required sizes.
- `tools/release upload games/<slug> [--preview]`: upload a build to the staging branch.

## Rules that hold in every session

- A human pays fees, accepts agreements, approves store copy and presses Release.
- Never type a password, bank number or tax ID into a website.

## What we learn lives in skills

What we learn lives in `.claude/skills/`. Read a skill before you work in its area, add what you learn to the skill it belongs in, and fix anything stale as soon as you notice it. This file stays under 80 lines.
