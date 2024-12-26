import unittest

from nodes.parentnode import ParentNode
from nodes.leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_init(self):
        node = ParentNode("div", [], { "class": "custom" })
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, { "class": "custom" })

    def test_error_if_no_required_props(self):
        with self.assertRaises(TypeError):
            ParentNode()

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, " Normal text "),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b> Normal text <i>italic text</i>Normal text</p>")

    def test_to_html_with_props(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, " Normal text "),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            { "class": "custom" }
        )

        self.assertEqual(node.to_html(), '<p class="custom"><b>Bold text</b> Normal text <i>italic text</i>Normal text</p>')

    def test_error_if_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, []).to_html()

    def test_error_if_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", []).to_html()

if __name__ == "__main__":
    unittest.main()

