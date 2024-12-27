"""
Defines the different types of text nodes
"""

from enum import Enum


class TextType(Enum):
    """
    Provides the different types of text that can exist
    """

    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    """
    Describes the text format
    """

    def __init__(self, text: str, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text_type == other.text_type

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
