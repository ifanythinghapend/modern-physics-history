"""Regression checks for broken references and link-probe edge cases."""
from pathlib import Path
import sys
import unittest
from urllib.error import HTTPError
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from project import LINK, validate_registry, validate_documents, validate
from check_links import classify, probe

class ReferencesTest(unittest.TestCase):
    def test_duplicate_reference_ids_are_rejected(self):
        records=[{'id':'001','url':'https://example.org/a'},{'id':'001','url':'https://example.org/b'}]
        self.assertTrue(any('编号重复' in e for e in validate_registry(records)))

    def test_link_must_point_to_anchor_in_its_target_file(self):
        docs={'chapters/a.md':'<a id="q-a"></a>\n[错误](../appendices/b.md#q-a)',
              'appendices/b.md':'<a id="ref-001"></a>'}
        self.assertTrue(validate_documents(docs))

    def test_valid_cross_file_link(self):
        docs={'chapters/a.md':'<a id="q-a"></a>\n[资料](../appendices/b.md#ref-001)',
              'appendices/b.md':'<a id="ref-001"></a>'}
        self.assertEqual(validate_documents(docs),[])

    def test_repeated_anchor_in_one_file_is_rejected(self):
        self.assertTrue(validate_documents({'a.md':'<a id="x"></a>\n<a id="x"></a>'}))

    def test_parentheses_and_chinese_text_do_not_swallow_adjacent_links(self):
        text='[甲](https://example.org/a(1905))以及[乙](https://example.org/b)。'
        self.assertEqual([m[1] for m in LINK.finditer(text)],['https://example.org/a(1905)','https://example.org/b'])

    def test_rate_limit_and_access_denial_are_not_broken_links(self):
        for code in (401,403,429,500,503):self.assertEqual(classify(code),'inconclusive')
        self.assertEqual(classify(404),'missing')
        self.assertEqual(classify(410),'missing')

    def test_head_405_falls_back_to_get(self):
        class Response:
            status=200
            url='https://example.org/test'
            def __enter__(self):return self
            def __exit__(self,*args):pass
        error=HTTPError('https://example.org/test',405,'method',None,None)
        with patch('check_links.urlopen',side_effect=[error,Response()]) as fetch:
            result=probe('https://example.org/test')
            self.assertEqual(result['status'],'reachable')
            self.assertEqual(fetch.call_args_list[1].args[0].get_method(),'GET')

    def test_current_manuscript_has_consistent_references(self):
        self.assertEqual(validate(),[])

if __name__=='__main__':unittest.main()
