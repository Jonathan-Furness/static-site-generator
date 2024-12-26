import unittest

from nodes.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_init(self):
        node = LeafNode("p", "This is a paragraph", { "class": "custom" })
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertEqual(node.props, { "class": "custom" })

    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph", { "class": "custom" })
        self.assertEqual(node.to_html(), '<p class="custom">This is a paragraph</p>')

    def test_error_if_no_required_props(self):
        with self.assertRaises(TypeError):
            LeafNode()

if __name__ == "__main__":
    unittest.main()
