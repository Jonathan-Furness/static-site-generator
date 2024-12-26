import unittest

from converters.split_link_nodes import split_link_nodes
from nodes.textnode import TextNode, TextType


class TestSplitLinkNodes(unittest.TestCase):
    def test_extract_links(self):
        node = TextNode(
            "This is text with a link [to google](https://www.google.com) and [to youtube](https://www.youtube.com/)",
            TextType.TEXT,
        )

        new_nodes = split_link_nodes([node])

        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to google", TextType.LINK, "https://www.google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/"),
        ]

        self.assertEqual(new_nodes, expected)

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_link_nodes([node])
        self.assertEqual(new_nodes, [node])

    def test_text_without_links(self):
        node = TextNode("This is plain text without any links", TextType.TEXT)
        new_nodes = split_link_nodes([node])
        self.assertEqual(new_nodes, [node])

    def test_non_text_node(self):
        # Should return unchanged for non-TEXT type nodes
        node = TextNode("![image](https://example.com/img.png)", TextType.IMAGE)
        new_nodes = split_link_nodes([node])
        self.assertEqual(new_nodes, [node])

    def test_multiple_nodes_input(self):
        nodes = [
            TextNode("Start ", TextType.TEXT),
            TextNode("[link](https://example.com)", TextType.TEXT),
            TextNode(" end", TextType.TEXT),
        ]
        new_nodes = split_link_nodes(nodes)
        expected = [
            TextNode("Start ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" end", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_consecutive_links(self):
        node = TextNode(
            "[link1](https://example1.com)[link2](https://example2.com)", 
            TextType.TEXT
        )
        new_nodes = split_link_nodes([node])
        expected = [
            TextNode("link1", TextType.LINK, "https://example1.com"),
            TextNode("link2", TextType.LINK, "https://example2.com"),
        ]
        self.assertEqual(new_nodes, expected)
