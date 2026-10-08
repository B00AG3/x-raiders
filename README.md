# X-Raiders

A browser port of the classic **Tomb Raider I** demo, ported and maintained by
[B00AG3](https://github.com/B00AG3). Explore the City of Vilcabamba, navigate its
ruins, jump across obstacles, and fight enemies directly in your browser.

**[Play X-Raiders in your browser](https://b00ag3.github.io/x-raiders/)**

The game starts automatically after the engine and demo data finish loading.
No installation is required. Click, tap, or press a key to enable sound if your
browser blocks audio autoplay. A modern browser with WebAssembly and WebGL is
required; a desktop keyboard is recommended.

## About the port

I adapted the X-Raiders engine for this browser release, added a self-contained
WebAssembly demo build, updated browser input handling, and set up automatic builds
and hosting on GitHub Pages. X-Raiders ships the Tomb Raider I PC demo's title data
and City of Vilcabamba level. It does not include the full retail game.

The browser launcher supports fullscreen and loading compatible level files from
your own copy of the game. Selected files are read locally by the browser.

## Controls

| Key | Action |
| --- | --- |
| Arrow keys | Move and turn |
| Space | Jump |
| Control | Action |
| Escape | Open inventory |
| Alt + Enter | Toggle fullscreen |
| Tab | Move focus out of the game to the page controls |

Click the game to return keyboard focus to it. Use **Go fullscreen** for an
immersive view, or **Load your own level** to select a `.PHD`, `.PSX`, `.TR2`, or
`.TR4` file between 1 KB and 64 MB. Compatibility depends on the level and any
additional assets it needs; the bundled demo works without additional files.

## Build and run locally

The GitHub Actions workflow uses **Emscripten 3.1.64**. With that SDK active and
Bash available, run from the repository root:

```sh
bash scripts/build-web.sh
python -m http.server 8000 --directory dist
```

Open [localhost:8000](http://localhost:8000). Serve `dist` over HTTP rather than
opening `index.html` directly. The output includes the launcher, JavaScript runtime,
WebAssembly module, preloaded demo data, and engine/asset notices.

## Hosting

The [Pages workflow](.github/workflows/pages.yml) builds and publishes the game on
every push to `master`, and can also be run manually from GitHub Actions.
GitHub Pages must use **GitHub Actions** as its build source. The generated `dist`
directory can also be hosted on a static web server that serves `.wasm` files with
the `application/wasm` MIME type.

## Sharing on X (desktop)

Share the normal game URL for an image link card. For an experimental Player Card,
share **https://b00ag3.github.io/x-raiders/x.html**. Its static HTML includes the
Player Card tags and a real game screenshot, with an 854 × 540 frame pointing to
`play.html`. The compact desktop player supports the existing keyboard controls,
fullscreen, and an **Open full game** link. Sound waits for a click or keypress.

The HTTPS player has no frame-blocking headers or sign-in requirement. This makes
it technically embeddable; it does not guarantee that X will display an inline
game. X has historically limited Player Cards to audio/video, and the former card
documentation now redirects. Its current policy prohibits bypassing card
limitations: https://docs.x.com/developer-terms/policy. Inline rendering needs
verification in an actual X post; a working iframe alone is not that verification.

The launcher requests a fresh `build.json` and loads one matching set of versioned
JavaScript, WebAssembly, and demo data. This prevents browsers from combining
cached engine files from different releases. Startup failures show their actual
error and a **Reload game** action. Desktop browsers with WebGL/WebAssembly are
the target; no new mobile UI is provided.

## Credits and licenses

X-Raiders builds on the original BSD 2-Clause engine; the engine copyright notice is retained in src/platform/web/ASSETS.md.
