"""
ParentNode is used to model HTML elements with child elements
"""

from .htmlnode import HTMLNode


class ParentNode(HTMLNode):
    """
    ParentNode is an HTML element that contains children
    """

    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is required")

        if not self.children:
            raise ValueError("Children is required")

        children = "".join([child.to_html() for child in self.children])

        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{children}</{self.tag}>"

        return f"<{self.tag}>{children}</{self.tag}>"
