import unittest

from nodes.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_has_url(self):
        node = TextNode("This is a text node", TextType.BOLD, url="https://www.google.com")
        self.assertEqual(node.url, "https://www.google.com")

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_text_type(self):
        for text_type in TextType:
            node = TextNode("This is a text node", text_type)
            self.assertEqual(node.text_type, text_type)


if __name__ == "__main__":
    unittest.main()
