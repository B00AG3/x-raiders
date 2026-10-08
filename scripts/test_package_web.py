import json
from pathlib import Path
import tempfile
import unittest

from package_web import package_web


class PackageWebTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.output = self.root / "dist"
        self.output.mkdir()
        self.template = self.root / "index.html"
        self.template.write_text(
            '<html lang="en"><head><meta name="twitter:card" content="summary_large_image">'
            '<link rel="canonical" href="https://b00ag3.github.io/x-raiders/">'
            '<meta property="og:url" content="https://b00ag3.github.io/x-raiders/">'
            '</head><body></body></html>', encoding="utf-8")
        self.template.with_name("preview.png").write_bytes(b"preview fixture")
        (self.output / "xraiders_wasm.js").write_text(
            'var wasm="xraiders_wasm.wasm", data="xraiders_wasm.data";', encoding="utf-8")
        (self.output / "xraiders_wasm.wasm").write_bytes(b"wasm fixture")
        (self.output / "xraiders_wasm.data").write_bytes(b"data fixture")

    def test_matching_assets_and_repeatable_packaging(self):
        release = package_web(self.output, self.template)
        self.assertEqual(release, package_web(self.output, self.template))
        self.assertEqual(release, json.loads((self.output / "build.json").read_text()))
        stem = Path(release["engine"]).stem
        engine = (self.output / release["engine"]).read_text()
        for extension in ("wasm", "data"):
            self.assertIn(f"{stem}.{extension}", engine)
            self.assertEqual((self.output / f"{stem}.{extension}").read_bytes(),
                             (self.output / f"xraiders_wasm.{extension}").read_bytes())
        self.assertNotIn("xraiders_wasm.", engine)
        self.assertIn('class="embedded"', (self.output / "play.html").read_text())
        share = (self.output / "x.html").read_text()
        self.assertIn('name="twitter:card" content="player"', share)
        self.assertIn('name="twitter:player"', share)
        self.assertIn('href="https://b00ag3.github.io/x-raiders/x.html"', share)
        self.assertIn('content="summary_large_image"', (self.output / "index.html").read_text())

    def test_engine_change_gets_a_new_bundle_url(self):
        before = package_web(self.output, self.template)
        (self.output / "xraiders_wasm.wasm").write_bytes(b"updated engine fixture")
        after = package_web(self.output, self.template)
        self.assertNotEqual(before["engine"], after["engine"])
        self.assertNotEqual(before["version"], after["version"])


if __name__ == "__main__":
    unittest.main()
