import unittest

from converters.markdown_blocks_and_types import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_should_convert_to_blocks(self):
        document = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

        blocks = markdown_to_blocks(document)

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item""",
        ]

        self.assertEqual(blocks, expected)

    def test_should_return_empty_array_if_all_whitespace(self):

        document = "     \n\n\n      \n"

        blocks = markdown_to_blocks(document)

        expected = []

        self.assertEqual(blocks, expected)

    def should_return_one_block_if_no_whitespace(self):

        document = "This is a full block of text.\nIt should only return one block."

        blocks = markdown_to_blocks(document)

        expected = ["This is a full block of text.\nIt should only return one block."]

        self.assertEqual(blocks, expected)
