"""
This module converts a fulline markdown file to HTMLNodes
"""

import re
from typing import Literal

from converters.text_to_textnodes import text_to_textnodes
from nodes.leafnode import LeafNode
from nodes.parentnode import ParentNode
from nodes.textnode import TextNode, TextType

from .markdown_blocks_and_types import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
)


def text_type_to_html_tag(text_type: TextType):
    """
    Returns the correct HTMline tag based on the text_type
    """
    match text_type:
        case TextType.TEXT:
            return None
        case TextType.BOLD:
            return "b"
        case TextType.ITALIC:
            return "i"
        case TextType.CODE:
            return "code"
        case TextType.IMAGE:
            return "img"
        case TextType.LINK:
            return "a"
        case _:
            raise ValueError("Invalid text_type")


def text_to_children(text: str):
    """
    Converts string into LeafNodes
    """
    text_nodes: list[TextNode] = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        tag = text_type_to_html_tag(node.text_type)
        value = node.text
        props = None

        if node.text_type == TextType.IMAGE:
            props = {"alt": node.text, "src": node.url}
            value = None
        elif node.text_type == TextType.LINK:
            props = {"href": node.url}

        children.append(LeafNode(tag, value, props))
    return children


def create_list_items(block: str, block_type: Literal[BlockType.OL, BlockType.UL]):
    """
    Converts ordered or unordered list blocks to respective list items
    """
    lines = block.split("\n")

    if block_type == BlockType.OL:
        text = [re.sub(r"^([0-9]\. )", "", line) for line in lines]
    else:
        text = [re.sub(r"^([\*\-] )", "", line) for line in lines]

    return [ParentNode(tag="li", children=text_to_children(li)) for li in text]


def block_to_html_node(block: str):
    """
    Converts markdown blocks into HTMLNodea
    """
    match block_to_block_type(block):
        case BlockType.HEADING:
            hashes = re.findall(r"^(#{1,6} )", block)[0]
            tag = f"h{len(hashes.strip())}"
            text = re.sub(r"^(#{1,6} )", "", block)
            return ParentNode(tag=tag, children=text_to_children(text))
        case BlockType.CODE:
            # Code is pre-formatted so remove the backticks and
            # use as LeafNode Value
            code_text = re.sub(r"^`{3}|`{3}$", "", block)
            text_node = LeafNode(tag=None, value=code_text)
            code_block = ParentNode(tag="code", children=[text_node])
            return ParentNode(tag="pre", children=[code_block])
        case BlockType.QUOTE:
            lines = block.split("\n")
            cleaned = list(map(lambda line: re.sub(r"^> ", "", line), lines))
            return LeafNode(tag="blockquote", value="".join(cleaned))
        case BlockType.OL:
            list_items = create_list_items(block, BlockType.OL)
            return ParentNode(tag="ol", children=list_items)
        case BlockType.UL:
            list_items = create_list_items(block, BlockType.UL)
            return ParentNode(tag="ul", children=list_items)
        case BlockType.PARAGRAPH:
            return ParentNode(tag="p", children=text_to_children(block))
        case _:
            raise ValueError("Invalid")


def markdown_to_html_node(markdown: str):
    """
    Converts markdown document to HTML
    """
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(b) for b in blocks]
    return ParentNode(tag="div", children=children).to_html()
