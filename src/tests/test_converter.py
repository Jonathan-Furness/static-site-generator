import unittest

from converters.text_node_to_html_node import text_node_to_html_node
from nodes.textnode import TextNode, TextType
from nodes.leafnode import LeafNode

class TestConverter(unittest.TestCase):
    def test_normal_text(self):
        text_node = TextNode("This is normal text", TextType.TEXT)
        converted = text_node_to_html_node(text_node)

        expected = LeafNode(None, "This is normal text")

        self.assertEqual(converted.to_html(), expected.to_html())

    def test_bold_text(self):
        text_node = TextNode("This is bold text", TextType.BOLD)
        converted = text_node_to_html_node(text_node)
        expected = LeafNode("b", "This is bold text")

        self.assertEqual(converted.to_html(), expected.to_html())

    def test_italic_text(self):
        text_node = TextNode("This is italic text", TextType.ITALIC)
        converted = text_node_to_html_node(text_node)
        expected = LeafNode("i", "This is italic text")

        self.assertEqual(converted.to_html(), expected.to_html())

    def test_code_text(self):
        text_node = TextNode("This is code text", TextType.CODE)
        converted = text_node_to_html_node(text_node)
        expected = LeafNode("code", "This is code text")

        self.assertEqual(converted.to_html(), expected.to_html())

    def test_link_text(self):
        text_node = TextNode("This is a link", TextType.LINK, "https://www.google.com")
        converted = text_node_to_html_node(text_node)
        expected = LeafNode("a", "This is a link", { "href": "https://www.google.com" })

        self.assertEqual(converted.to_html(), expected.to_html())

    def test_image_text(self):
        text_node = TextNode("This is an image", TextType.IMAGE, "https://www.google.com")
        converted = text_node_to_html_node(text_node)
        expected = LeafNode("img", "", { "src": "https://www.google.com", "alt": "This is an image" })

        self.assertEqual(converted.to_html(), expected.to_html())

    def test_is_not_valid_type(self):
        text_node = TextNode("This is an image", "not_valid", "https://www.google.com")
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)
