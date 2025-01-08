import unittest

from converters.markdown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_should_parse_p_tags(self):

        test = "This is a paragraph\n\nThis is another paragraph"

        html = markdown_to_html_node(test)

        expected = (
            "<div><p>This is a paragraph</p><p>This is another paragraph</p></div>"
        )

        self.assertEqual(html, expected)

    def test_should_parse_headings(self):

        test = "\n\n".join(
            [
                "# This is a h1",
                "## This is a h2",
                "### This is a h3",
                "#### This is a h4",
                "##### This is a h5",
                "###### This is a h6",
                "####### This is a p",
            ]
        )

        html = markdown_to_html_node(test)

        expected = "".join(
            [
                "<div>",
                "<h1>This is a h1</h1>",
                "<h2>This is a h2</h2>",
                "<h3>This is a h3</h3>",
                "<h4>This is a h4</h4>",
                "<h5>This is a h5</h5>",
                "<h6>This is a h6</h6>",
                "<p>####### This is a p</p>",
                "</div>",
            ]
        )

        self.assertEqual(html, expected)

    def test_should_parse_ordered_list(self):

        test = "\n".join(
            [
                "1. This is the first item",
                "2. This is the second item",
                "3. This is the third item",
            ]
        )

        html = markdown_to_html_node(test)

        expected = "".join(
            [
                "<div>",
                "<ol>",
                "<li>This is the first item</li>",
                "<li>This is the second item</li>",
                "<li>This is the third item</li>",
                "</ol>",
                "</div>",
            ]
        )

        self.assertEqual(html, expected)

    def test_should_parse_unordered_list(self):

        test = "\n".join(
            [
                "* This is the first item",
                "* This is the second item",
                "- This is the third item",
            ]
        )

        html = markdown_to_html_node(test)

        expected = "".join(
            [
                "<div>",
                "<ul>",
                "<li>This is the first item</li>",
                "<li>This is the second item</li>",
                "<li>This is the third item</li>",
                "</ul>",
                "</div>",
            ]
        )

        self.assertEqual(html, expected)

    def test_should_parse_code_block(self):
        test = "```\nconst num = 1\n```"

        html = markdown_to_html_node(test)

        expected = "".join(
            [
                "<div>",
                "<pre>",
                "<code>",
                "\nconst num = 1\n",
                "</code>",
                "</pre>",
                "</div>",
            ]
        )

        self.assertEqual(html, expected)

    def test_should_parse_blockquote(self):

        test = "> This is a quote\n> This is the second line\n> This is the third line"

        html = markdown_to_html_node(test)

        expected = "".join(
            [
                "<div>",
                "<blockquote>",
                "This is a quote",
                "This is the second line",
                "This is the third line",
                "</blockquote>",
                "</div>",
            ]
        )

        self.assertEqual(html, expected)

    def test_should_parse_document(self):

        paragraphs = "This is a paragraph\n\nThis is another paragraph"
        headings = "\n\n".join(
            [
                "# This is a h1",
                "## This is a h2",
                "### This is a h3",
                "#### This is a h4",
                "##### This is a h5",
                "###### This is a h6",
                "####### This is a p",
            ]
        )
        ordered_list = "\n".join(
            [
                "1. This is the first item",
                "2. This is the second item",
                "3. This is the third item",
            ]
        )

        unordered_list = "\n".join(
            [
                "* This is the first item",
                "* This is the second item",
                "- This is the third item",
            ]
        )
        code_block = "```\nconst num = 1\n```"
        block_quote = (
            "> This is a quote\n> This is the second line\n> This is the third line"
        )

        test = "\n\n".join(
            [
                paragraphs,
                headings,
                ordered_list,
                unordered_list,
                code_block,
                block_quote,
            ]
        )

        html = markdown_to_html_node(test)

        expected_paragaphs = (
            "<p>This is a paragraph</p><p>This is another paragraph</p>"
        )

        expected_headings = "".join(
            [
                "<h1>This is a h1</h1>",
                "<h2>This is a h2</h2>",
                "<h3>This is a h3</h3>",
                "<h4>This is a h4</h4>",
                "<h5>This is a h5</h5>",
                "<h6>This is a h6</h6>",
                "<p>####### This is a p</p>",
            ]
        )

        expected_ol = "".join(
            [
                "<ol>",
                "<li>This is the first item</li>",
                "<li>This is the second item</li>",
                "<li>This is the third item</li>",
                "</ol>",
            ]
        )
        expected_ul = "".join(
            [
                "<ul>",
                "<li>This is the first item</li>",
                "<li>This is the second item</li>",
                "<li>This is the third item</li>",
                "</ul>",
            ]
        )
        expected_code = "".join(
            [
                "<pre>",
                "<code>",
                "\nconst num = 1\n",
                "</code>",
                "</pre>",
            ]
        )

        expected_quote = "".join(
            [
                "<blockquote>",
                "This is a quote",
                "This is the second line",
                "This is the third line",
                "</blockquote>",
            ]
        )

        expected = "".join(
            [
                "<div>",
                expected_paragaphs,
                expected_headings,
                expected_ol,
                expected_ul,
                expected_code,
                expected_quote,
                "</div>",
            ]
        )

        self.assertEqual(html, expected)

    def test_should_parse_markdown_href(self):

        test = "**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)"

        html = markdown_to_html_node(test)

        expected = "<div><p><b>I like Tolkien</b>. Read my <a href=\"/majesty\">first post here</a> (sorry the link doesn't work yet)</p></div>"

        self.assertEqual(html, expected)

    def test_should_create_blockquote(self):
        test = "> All that is gold does not glitter"

        html = markdown_to_html_node(test)

        expected = "<div><blockquote>All that is gold does not glitter</blockquote></div>"

        self.assertEqual(html, expected)
