# Builds and branches

## The flow

```
tools/release export games/<slug>            # writes steam/build/<platform>
tools/release upload games/<slug> --preview  # writes logs and a manifest, uploads nothing
tools/release upload games/<slug>            # uploads and sets live on staging
```

## Not obvious

- The default branch cannot be set live from steamcmd, so the tool drops that flag on purpose. Promote builds in Steamworks under SteamPipe, then Builds.
- Create the password protected `staging` branch once, before the first upload.
- Never type the build account password. If the tool reports no cached login, give a human the one command it prints.
- Use a separate build account with only the publish permissions, not the account that owns the studio.
- `steam_appid.txt` and `*.pdb` files never ship.

## steam.json

```json
{ "name": "...", "appId": 0, "depots": { "windows": 0, "linux": 0 }, "betaBranch": "staging" }
```

The tool refuses to upload while `appId` is 0. A `null` depot is skipped, which is how you ship without a platform.

Source: [uploading](https://partner.steamgames.com/doc/sdk/uploading).
