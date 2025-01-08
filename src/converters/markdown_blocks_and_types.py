"""
This module is used to extract markdown blocks and block types
from markdown documents
"""

import re
from enum import Enum


class BlockType(Enum):
    """
    Types used to describe Markdown blocks
    """

    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"


def markdown_to_blocks(document: str):
    """
    Takes in markdown as a string and returns an array of markdown blocks
    """
    lines = document.split("\n\n")
    stripped = map(lambda x: x.strip(), lines)
    filtered = filter(bool, stripped)
    return list(filtered)


def is_heading_block(text: str):
    """
    Determines whether the text is a heading block
    """
    return re.match(r"^(#{1,6}) ([\s\S]*)", text)


def is_code_block(text: str):
    """
    Determines whether the text is a code block
    """
    return re.match(r"^(`{3})([\s\S]*)(`{3})$", text)


def is_quote_block(text: str):
    """
    Determines whether the text is a quote block
    """
    return re.match(r"^(> )([\s\S]*)", text)


def is_ol_block(text: str, item_num: int = 1):
    """
    Determines whether the text starts with ordered_list character
    and ensures the item_number matches
    """
    matcher = re.match(r"^([0-9]{1,})\. ([\s\S]*)", text)
    return matcher and int(matcher.group()[0]) == item_num


def is_ul_block(text: str):
    """
    Determines whether the text starts with unordered_list character
    """
    return re.match(r"^[\*\-] ([\s\S]*)", text)


def block_to_block_type(block: str):
    """
    Determines the block type of a Markdown block
    """
    if is_heading_block(block):
        return BlockType.HEADING

    if is_code_block(block):
        return BlockType.CODE

    if is_quote_block(block):
        every_line_quote = all(is_quote_block(line) for line in block.split("\n"))

        if every_line_quote:
            return BlockType.QUOTE

    if is_ol_block(block):
        every_line_ol = all(
            is_ol_block(line, item_num=i + 1)
            for i, line in enumerate(block.split("\n"))
        )

        if every_line_ol:
            return BlockType.OL

    if is_ul_block(block):
        every_line_ul = all(is_ul_block(line) for line in block.split("\n"))

        if every_line_ul:
            return BlockType.UL
    return BlockType.PARAGRAPH
