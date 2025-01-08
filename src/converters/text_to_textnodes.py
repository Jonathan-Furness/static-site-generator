"""
Converts text to an array of TextNodes
"""

from nodes.textnode import TextNode, TextType

from .split_image_nodes import split_image_nodes
from .split_link_nodes import split_link_nodes
from .split_nodes_delimiter import split_nodes_delimiter


def text_to_textnodes(text: str):
    """
    Converts text to array of TextNodes
    """
    node = TextNode(text, TextType.TEXT)
    images = split_image_nodes([node])
    links = split_link_nodes(images)
    bold = split_nodes_delimiter(links, "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    return code 
