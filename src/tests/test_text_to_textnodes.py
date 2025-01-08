import unittest

from converters.text_to_textnodes import text_to_textnodes
from nodes.textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_should_convert_text(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://google.com)"

        nodes = text_to_textnodes(text)

        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://google.com"),
        ]

        self.assertEqual(nodes, expected)

    def test_empty_text(self):
        text = ""
        nodes = text_to_textnodes(text)
        expected = []
        self.assertEqual(nodes, expected)

    def test_multiple_bold_sections(self):
        text = "Start **bold** middle **also bold** end"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Start ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" middle ", TextType.TEXT),
            TextNode("also bold", TextType.BOLD),
            TextNode(" end", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)

    def test_nested_formatting(self):
        text = "This is **bold with _italic_ inside**"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold with ", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode(" inside", TextType.BOLD),
        ]
        self.assertEqual(nodes, expected)

    def test_multiple_images(self):
        text = "![first](image1.jpg) normal text ![second](image2.jpg)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("first", TextType.IMAGE, "image1.jpg"),
            TextNode(" normal text ", TextType.TEXT),
            TextNode("second", TextType.IMAGE, "image2.jpg"),
        ]
        self.assertEqual(nodes, expected)

    def test_incomplete_formatting(self):
        text = "This has _incomplete formatting"
        with self.assertRaises(Exception) as context:
            text_to_textnodes(text)
        self.assertTrue("Invalid Markdown syntax" in str(context.exception))
