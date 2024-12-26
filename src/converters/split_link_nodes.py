from nodes.textnode import TextNode, TextType

from .extract_markdown import extract_markdown_links


def split_link_nodes(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue

        text = node.text

        parts = []
        for link in links:
            link_text = link[0]
            url = link[1]
            link_string = f"[{link_text}]({url})"
            split_parts = text.split(link_string, 1)
            if split_parts[0]:
                parts.append(TextNode(split_parts[0], TextType.TEXT))
            parts.append(TextNode(text=link_text, text_type=TextType.LINK, url=url))

            text = split_parts[1] if len(split_parts) > 1 else ""

        if text:
            parts.append(TextNode(text, TextType.TEXT))

        new_nodes.extend(parts)

    return new_nodes
