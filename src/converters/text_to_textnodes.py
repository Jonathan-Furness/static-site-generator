from nodes.textnode import TextNode, TextType

from .split_image_nodes import split_image_nodes
from .split_link_nodes import split_link_nodes
from .split_nodes_delimiter import split_nodes_delimiter


def text_to_textnodes(text: str):
    node = TextNode(text, TextType.TEXT)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "*", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    images = split_image_nodes(code)
    links = split_link_nodes(images)
    return links
