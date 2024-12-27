"""
HTMLNode is inheriter by ParentNode and LeafNode.
It defines the basics on an HTML element
"""

from functools import reduce


class HTMLNode:
    """
    This is a HTML element
    """

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Converts the nodes into HTML
        """
        raise NotImplementedError()

    def props_to_html(self):
        """
        Converts the properties into correct HTML
        """
        if self.props is None:
            return ""
        return reduce(
            lambda acc, x: f'{acc} {x[0]}="{x[1]}"' if acc else f'{x[0]}="{x[1]}"',
            self.props.items(),
            "",
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
