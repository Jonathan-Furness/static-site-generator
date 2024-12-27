"""
LeafNode is used for HTML elements that do not have children
"""

from .htmlnode import HTMLNode


class LeafNode(HTMLNode):
    """
    LeafNode models an HTML element without children
    """

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.tag is None:
            return self.value
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
