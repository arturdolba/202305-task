'''
Unit tests for program.
'''

import unittest

from modules.functions import *

class TestClearDocument(unittest.TestCase):
    def test_clear_document_empty_string(self):
        '''
        Test clear_document with empty string.
        '''
        result = clear_document("")
        self.assertEqual(result, "")

    def test_clear_document_empty_string_stripped(self):
        '''
        Test clear_document with string which should be empty after strip
        '''
        result = clear_document(" \n")
        self.assertEqual(result, "")

    def test_clear_document_easy_html(self):
        '''
        Test clear_dopcument for HTML tag containing some text.
        '''
        result = clear_document("<p>def</p>")
        self.assertEqual(result, "def")

    def test_clear_document_not_ended_tag(self):
        '''
        Check clear_document for unfinished tag startred with "<"
        '''
        result = clear_document("<abc123 456!")
        self.assertEqual(result,"<abc123 456!")

    def test_clear_document_not_started_tag(self):
        '''
        Check clear_document for ">" character which is not part of tag.
        '''
        result = clear_document("abc>def")
        self.assertEqual(result, "abc>def")

    def test_clear_document_quotes_1(self):
        '''
        Check clear_document for ignoring ">" in tag which is in quote of tag element.
        '''
        result = clear_document("<a href='abc>'>abc</a>")
        self.assertEqual(result, "abc")

    def test_clear_document_quotes_2(self):
        '''
        Check clear_document for ignoring "<" in tag which is in quote of tag element.
        '''
        result = clear_document('<a href="abc<input">def</a>')
        self.assertEqual(result, "def")

    def test_clear_document_script(self):
        '''
        Check clear_document with code in JavaScript.
        '''
        result = clear_document("""abc<script type='text/javascript'>
        var x=0; if (a>2) alert('abc');</script>""")
        self.assertEqual(result,"abc")

    def test_clear_document_style(self):
        '''
        Check clear_document with code in CSS
        '''
        result = clear_document("<style> h1 { font-size: 2 }</style>")
        self.assertEqual(result,"")

    def test_clear_document_script_with_code_quoting(self):
        '''
        Check clear_document with quoted ending tag of script, which should be ignored.
        '''
        result = clear_document("<script> a = '</script>'abc</script>")
        self.assertEqual(result,"")

    def test_clear_document_complex_test(self):
        '''
        Check clear_document for complex HTML document.
        '''
        result = clear_document("<html><head><title>This is document</title>"+
                                "</head><body><script>some data in script</script>"+
                                "<p>TEST</p></body></html>")
        self.assertEqual(result,"This is document TEST")

    def test_clear_text_entity(self):
        """
        Check clear_text for removing HTML entity.
        """
        result = clear_text("abc&gte;def")
        self.assertEqual(result, "abc def")

    def test_clear_text_special_chars(self):
        '''
        Check clear_text for removing special chars.
        '''
        result = clear_text("a ;bc x, ;")
        self.assertEqual(result.strip(),"a  bc x")

    def test_clear_text__special_chars_2(self):
        '''
        Check clear_text for removing special chars, more complex.
        '''
        result = clear_text("!@#a35*#$")
        self.assertEqual(result.strip(),"a35")

    def test_clear_text_improper_entity(self):
        '''
        Check clear_text for ignoring improper entities and get text from them.
        '''
        result = clear_text("& abc ;")
        self.assertEqual(result.strip(), "abc")

    def test_divide_to_words(self):
        '''
        Test divide_to_words for dividing string to words, where space is separator.
        '''
        result = divide_to_words("abc def! ghi@ a@  cxy")
        self.assertEqual(result,["abc", "def!", "ghi@", "a@", "cxy"])

    def test_lowercase_words(self):
        '''
        Test lowercase_words - it should change words in list to lowercase.
        '''
        result = lowercase_words(["Czy", "to", "działa", "Tak", "Jest", "OK"])
        self.assertEqual(result,["czy", "to", "działa", "tak", "jest", "ok"])

    def test_top_words(self):
        '''
        Test top_words - it should count and sort words by frequency descending and then by word ascending.
        '''
        result = top_words(
            ['d', 'd', "abc", "def", "ghi",
             "abc", "def", "ghi", 'd', 'd', 
             "erp", "volvo", "polska"], 10)
        self.assertEqual(result, [
            ['d', 4],
            ["abc", 2],
            ["def", 2],
            ['ghi', 2],
            ['erp', 1],
            ['polska', 1],
            ['volvo', 1]])

if __name__ == '__main__':
    unittest.main()
