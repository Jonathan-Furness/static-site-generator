import unittest

from converters.markdown_blocks_and_types import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_should_detect_heading(self):

        tests = [
            "# This is a h1",
            "## This is a h2",
            "### this is a h3",
            "#### This is a h4",
            "##### this is a h5",
            "###### this is a h6",
            "####### this is a paragraph",
        ]

        expected_headings = [BlockType.HEADING for _ in range(6)]
        expected_headings.append(BlockType.PARAGRAPH)

        block_types = [block_to_block_type(b) for b in tests]

        self.assertEqual(block_types, expected_headings)

    def test_should_detect_code(self):

        tests = [
            "```variable = 3.14```",
            "```\n\nvariable = 4.14\n\ntext='some text'```",
            "`inline code block`",
        ]

        expected_code = [BlockType.CODE, BlockType.CODE, BlockType.PARAGRAPH]

        block_types = [block_to_block_type(b) for b in tests]

        self.assertEqual(block_types, expected_code)

    def test_should_detect_quote(self):

        tests = [
            "> This is a quote\n> This is another line in the quote\n> This is the last line in the quote",
            "> This is a quote\nThis is just a new paragraph line",
            "This is just a paragraph",
        ]

        expected_types = [BlockType.QUOTE, BlockType.PARAGRAPH, BlockType.PARAGRAPH]

        block_types = [block_to_block_type(b) for b in tests]

        self.assertEqual(block_types, expected_types)

    def test_should_detect_ol(self):

        tests = [
            "1. First point\n2. Second point\n3. Final point",
            "2. Second point\n1. First point\n3. Final Point",
            "1.First point\n2. Second point\n3. Final point",
            "First point\n2. second point\n3. Final point",
            "1) First point\n2. Second point\n3. Final point",
        ]

        expected_types = [BlockType.OL]
        expected_types.extend([BlockType.PARAGRAPH for _ in range(4)])

        block_types = [block_to_block_type(b) for b in tests]

        self.assertEqual(block_types, expected_types)
