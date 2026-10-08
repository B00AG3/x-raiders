# Browser hosting contract

Purpose: publish this repository's browser game build under B00AG3,
with a playable Tomb Raider I PC demo and automatic rebuilds after source changes.
Surface: game player (operate/showcase). This is a hosting adaptation, not a redesign.

Keep the incumbent canvas-first HTML interface and native browser controls.
The game is the signature visual; no marketing sections, decorative motion,
brand logos, invented statistics, or new component library are introduced.
Native system controls and the existing game UI remain the implementation source.

Foundation: white page, black text, black canvas, native control colors.
Typography: system sans-serif for the shell; original engine typography in game.
Spacing: 1rem page padding, compact controls; canvas dominates available width.
Responsive: canvas fits the viewport; controls wrap; retain browser zoom.
Fullscreen uses the browser's canvas fullscreen API. No decorative animation.
Keyboard events belong to the focused canvas, leaving links and controls usable.

Required states: engine loading, automatic start, playing, load/error recovery,
disabled controls while loading, visible keyboard focus, WebGL failure.

Source map:
- Shell, canvas, fullscreen, file loading, audio: src/platform/web/index.html
  (BSD 2-Clause; notice retained in src/platform/web/ASSETS.md).
- Game: src/platform/web/main.cpp, existing X-Raiders engine, updated Emscripten selectors.
- Demo data: Lost Artefacts TRX demo archive; see src/platform/web/ASSETS.md.
- Browser port: B00AG3; standalone repository https://github.com/B00AG3/x-raiders.

Scope exception: existing interface retained; no new layout or catalog equivalents
needed for this deployment. No brand assets are used. Preserve engine license and
asset attribution in README.md, LICENSE, and src/platform/web/ASSETS.md, with
LICENSE.txt and ASSETS.txt shipped alongside the browser build. The user requested
removing the visible repository/credits footer and Start button. Keep the existing
canvas and native fullscreen/file controls. No new component roles or layout are
introduced by this narrow change. Audio unlocks on the first click, tap, or keypress.
Desktop focus enters the canvas when ready only if the user has not focused another
control; mobile startup does not force focus. Engine rendering is essential game
motion; Escape opens the inventory. No decorative shell motion is added.

Desktop X sharing extension: retain the approved shell and engine. `x.html` uses
experimental Player Card metadata; `play.html` reuses the same HTML in a compact
854 × 540 frame with the original fullscreen control, a native full-game link,
and visible status/recovery. The default page uses an image link card. This is a
metadata/embedding adaptation, not a new visual identity. No mobile changes are
in scope. No X logo, other company marks, new icon family, catalog component,
marketing layout, or decorative assets are introduced. The existing native
controls and engine are the verified reused sources; the preview is an actual
desktop game screenshot in src/platform/web/preview.png. The packager generates
all three pages from src/platform/web/index.html, preventing shell divergence.

Reliability: the launcher obtains fresh release metadata and loads content-versioned
engine/data files together; error messages expose the failure and enable retry.
The compact frame fills its available height; error copy wraps rather than clips.
Audio remains suspended until a user interaction. Retain keyboard focus visibility
and Tab escape from the canvas. Test normal and compact desktop widths, warm/cold
startup, missing-manifest recovery, and iframe permissions. X inline rendering
is a platform-controlled outcome and must not be reported as verified without an
actual post.
