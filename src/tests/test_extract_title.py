import unittest

from src.generate.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_should_extract_title(self):

        markdown = "# This is the title"

        extracted = extract_title(markdown)

        expected = "This is the title"

        self.assertEqual(extracted, expected)

    def test_should_clean_all_spaces(self):

        markdown = "#   This is the title   "

        extracted = extract_title(markdown)

        expected = "This is the title"

        self.assertEqual(extracted, expected)

    def test_should_handle_multiple_lines(self):

        markdown = "# This is the title\n### This is a sub title\n\nThis is a paragraph"

        extracted = extract_title(markdown)

        expected = "This is the title"

        self.assertEqual(extracted, expected)

    def test_should_handle_no_title(self):

        markdown = "This is some text"

        with self.assertRaises(ValueError):
            extract_title(markdown)
