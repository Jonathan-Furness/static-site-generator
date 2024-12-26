from nodes.textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        splits = node.text.split(delimiter)
        if len(splits) % 2 == 0:
            raise Exception(
                f"Invalid Markdown syntax: Expected closing delimiter {delimiter}"
            )
            
        for i, text in enumerate(splits):
            if text == "":
                continue
            if i % 2 == 0:
                # Process regular text for nested delimiters
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                # For text inside delimiters, recursively process for other delimiters
                if delimiter == "**" and "*" in text:  # Handle nested italic in bold
                    nested_nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "*", TextType.ITALIC)
                    for nested_node in nested_nodes:
                        if nested_node.text_type == TextType.TEXT:
                            new_nodes.append(TextNode(nested_node.text, text_type))
                        else:
                            new_nodes.append(nested_node)
                else:
                    new_nodes.append(TextNode(text, text_type))

    return new_nodes
