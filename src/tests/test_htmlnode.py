import unittest

from nodes.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init(self):
        node = HTMLNode("p", "This is a paragraph", [], { "class": "custom" })
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, { "class": "custom" })

    def test_default_init(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", [], { "class": "custom" })
        self.assertEqual(node.__repr__(), "HTMLNode(p, This is a paragraph, [], {'class': 'custom'})")

    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", [], { "class": "custom" })
        self.assertEqual(node.props_to_html(), 'class="custom"')
