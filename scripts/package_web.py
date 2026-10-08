"""Package one matching JS/WASM/data release and the desktop share/player pages."""
import argparse
import hashlib
import json
from pathlib import Path


def package_web(output: Path, template: Path) -> dict:
    original = "xraiders_wasm"
    files = {extension: (output / f"{original}.{extension}").read_bytes()
             for extension in ("js", "wasm", "data")}
    digest = hashlib.sha256(b"".join(files.values())).hexdigest()[:16]
    stem = f"xraiders-{digest}"
    runtime = files["js"].decode("utf-8")
    for extension in files:
        runtime = runtime.replace(f"{original}.{extension}", f"{stem}.{extension}")
    (output / f"{stem}.js").write_text(runtime, encoding="utf-8")
    for extension in ("wasm", "data"):
        (output / f"{stem}.{extension}").write_bytes(files[extension])
    # Retain the original files for older HTML during the first rollout.
    manifest = {"version": digest, "engine": f"{stem}.js"}
    (output / "build.json").write_text(json.dumps(manifest), encoding="utf-8")
    html = template.read_text(encoding="utf-8")
    (output / "index.html").write_text(html, encoding="utf-8")
    (output / "play.html").write_text(
        html.replace('<html lang="en">', '<html lang="en" class="embedded">'), encoding="utf-8")
    player_tags = '\n'.join([
        '<meta name="twitter:player" content="https://b00ag3.github.io/x-raiders/play.html">',
        '<meta name="twitter:player:width" content="854">',
        '<meta name="twitter:player:height" content="540">',
    ])
    share = html.replace('name="twitter:card" content="summary_large_image"',
                         'name="twitter:card" content="player"')
    share = share.replace('rel="canonical" href="https://b00ag3.github.io/x-raiders/"',
                          'rel="canonical" href="https://b00ag3.github.io/x-raiders/x.html"')
    share = share.replace('property="og:url" content="https://b00ag3.github.io/x-raiders/"',
                          'property="og:url" content="https://b00ag3.github.io/x-raiders/x.html"')
    share = share.replace('</head>', player_tags + '\n</head>')
    (output / "x.html").write_text(share, encoding="utf-8")
    preview = template.with_name("preview.png")
    (output / "preview.png").write_bytes(preview.read_bytes())
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("dist"))
    args = parser.parse_args()
    print(json.dumps(package_web(args.output, Path("src/platform/web/index.html"))))
