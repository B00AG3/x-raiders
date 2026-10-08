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

## Credits and licenses

X-Raiders builds on the original BSD 2-Clause engine; the engine copyright notice is retained in src/platform/web/ASSETS.md.