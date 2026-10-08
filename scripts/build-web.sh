#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
em++ src/platform/web/main.cpp src/libs/stb_vorbis/stb_vorbis.c src/libs/tinf/tinflate.c \
  -O3 -ffast-math -fmax-type-align=2 -std=c++11 -Wno-c++11-narrowing -Werror=extra-tokens \
  -Isrc -DOPENLARA_BROWSER_DEMO \
  -sALLOW_MEMORY_GROWTH=1 -sINITIAL_MEMORY=201326592 -sMAX_WEBGL_VERSION=2 \
  -sEXPORTED_FUNCTIONS='["_main","_malloc","_free"]' \
  -sEXPORTED_RUNTIME_METHODS='["ccall","callMain","getValue","writeArrayToMemory"]' \
  --preload-file src/platform/web/assets/level@/level \
  --preload-file src/platform/web/assets/audio@/audio \
  -o dist/xraiders_wasm.js
cp src/platform/web/index.html dist/index.html
cp LICENSE dist/LICENSE.txt
cp src/platform/web/ASSETS.md dist/ASSETS.txt
touch dist/.nojekyll
