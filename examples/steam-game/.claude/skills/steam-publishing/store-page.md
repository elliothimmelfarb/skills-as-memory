# Store page

## Art

Put art in `games/<slug>/steam/store-assets/` and check it with `tools/release assets`.

| File stem | Size | Rule |
|---|---|---|
| `header_capsule` | 920x430 | key art and logo |
| `small_capsule` | 462x174 | logo nearly fills it |
| `main_capsule` | 1232x706 | key art and logo |
| `vertical_capsule` | 748x896 | key art and logo |
| `library_capsule` | 600x900 | key art and logo |
| `library_hero` | 3840x1240 | no text at all |
| `screenshots/*` | at least 1920x1080, at least 5 | gameplay only |

Sizes checked 2026-10-30 against the [standard assets](https://partner.steamgames.com/doc/store/assets/standard) and [library assets](https://partner.steamgames.com/doc/store/assets/libraryassets) pages.

## Copy

Draft in `games/<slug>/store/`, and a human approves it before it goes up. Write the short description, the about text, the feature list, tags and system requirements. List only what is in the build, and leave out links to other sites.

## Filling the page

There is no API for store page content, so this is a browser step in a session where a human has signed in. Save as you go, because nothing is public until the page passes review and a human posts it as Coming Soon.

## Lessons

Add what reviewers rejected, and why, here.
