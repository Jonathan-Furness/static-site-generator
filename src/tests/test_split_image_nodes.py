import unittest

from converters.split_image_nodes import split_image_nodes
from nodes.textnode import TextNode, TextType


class TestSplitImageNodes(unittest.TestCase):
    def test_extracts_image(self):
        node = TextNode(
            "This is text with a link ![to google](https://www.google.com) and ![to youtube](https://www.youtube.com/)",
            TextType.TEXT,
        )

        new_nodes = split_image_nodes([node])

        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to google", TextType.IMAGE, "https://www.google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.IMAGE, "https://www.youtube.com/"
            ),
        ]

        self.assertEqual(new_nodes, expected)

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_image_nodes([node])
        self.assertEqual(new_nodes, [node])

    def test_no_images(self):
        node = TextNode("Just plain text without images", TextType.TEXT)
        new_nodes = split_image_nodes([node])
        self.assertEqual(new_nodes, [node])

    def test_multiple_nodes(self):
        nodes = [
            TextNode("First node ![alt1](url1)", TextType.TEXT),
            TextNode("Second node", TextType.TEXT),
            TextNode("Third node ![alt2](url2)", TextType.TEXT)
        ]
        new_nodes = split_image_nodes(nodes)
        expected = [
            TextNode("First node ", TextType.TEXT),
            TextNode("alt1", TextType.IMAGE, "url1"),
            TextNode("Second node", TextType.TEXT),
            TextNode("Third node ", TextType.TEXT),
            TextNode("alt2", TextType.IMAGE, "url2")
        ]
        self.assertEqual(new_nodes, expected)

    def test_non_text_node(self):
        node = TextNode("![alt](url)", TextType.IMAGE, "original_url")
        new_nodes = split_image_nodes([node])
        self.assertEqual(new_nodes, [node])

    def test_image_at_start(self):
        node = TextNode("![start](url1) middle ![end](url2)", TextType.TEXT)
        new_nodes = split_image_nodes([node])
        expected = [
            TextNode("start", TextType.IMAGE, "url1"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("end", TextType.IMAGE, "url2")
        ]
        self.assertEqual(new_nodes, expected)
