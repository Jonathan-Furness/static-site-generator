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

        html = f"<{self.tag}>"
        if self.props:
            html = f"<{self.tag} {self.props_to_html()}>"

        if self.value:
            html += f"{self.value}"

        html += f"</{self.tag}>"
        return html
