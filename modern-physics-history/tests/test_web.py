"""Regression checks for offline publication, broken anchors and dropped formulae."""
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from check_package import inspect_html,check

class ReadingPageTest(unittest.TestCase):
    def test_fragment_links_must_have_targets(self):
        _,errors=inspect_html('<a href="#missing">x</a>')
        self.assertTrue(any('锚点不存在' in error for error in errors))

    def test_same_document_svg_glyph_links_are_valid(self):
        _,errors=inspect_html('<svg><path id="glyph"/><use href="#glyph"/></svg>')
        self.assertEqual(errors,[])

    def test_external_citations_do_not_make_reading_depend_on_network(self):
        _,errors=inspect_html('<a href="https://example.org/paper">paper</a>')
        self.assertEqual(errors,[])

    def test_external_script_is_rejected(self):
        _,errors=inspect_html('<script src="https://example.org/math.js"></script>')
        self.assertTrue(any('外部资源' in error for error in errors))

    def test_missing_local_asset_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            _,errors=inspect_html('<img src="cover.png">',Path(folder))
            self.assertTrue(any('文件不存在' in error for error in errors))

    def test_current_reading_edition_is_complete(self):
        errors,_=check()
        self.assertEqual(errors,[])

if __name__=='__main__':unittest.main()
