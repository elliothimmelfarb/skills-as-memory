# Runbook: one game, from project to paid product

Track each game in `games/<slug>/LAUNCH.md`. Tick off phases there with dates and commit after each one, so the next session knows where things stand.

## Phase 1: ready for Steam

1. Add the Steam integration and keep the game fully playable when Steam is not running.
2. Export a build for this machine and run it.
3. Decide platforms. The default is Windows and Linux. Every platform on the page gets launched by the reviewer, so add macOS only if it runs well.

## Phase 2: App ID (a human pays)

1. Ask a human to pay the app fee as soon as the game is picked, because the waiting period starts there.
2. Read the App ID and depot IDs from Steamworks and write them into `steam/steam.json`.
3. Set one launch option per platform in the installation settings.

## Phase 3: store page (you draft, a human approves)

1. Make art until `tools/release assets` passes. Screenshots come from real play of the exported build.
2. Draft the copy in `games/<slug>/store/` and show it to a human.
3. After approval, fill the page, set a release date at least 3 weeks out, and mark it ready for review.
4. When the page is approved, ask whether to post it as Coming Soon. That is public, so a human decides.

## Phase 4: build

1. Run `tools/release upload games/<slug> --preview`, then upload to `staging`.
2. Install from `staging` on a real Steam client and check launch, overlay and achievements.
3. Set the build live on the default branch in Steamworks, then mark it ready for review.

## Phase 5: release (a human presses the button)

Check the three clocks in `requirements.md`. When they have all passed and the price is approved, ask a human to press Release.

## Phase 6: after release

Upload updates to `staging`, test them, then set them live. On a released app that step needs a mobile confirmation, so a human does it.
