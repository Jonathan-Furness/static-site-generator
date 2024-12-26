from nodes.textnode import TextNode, TextType

from .extract_markdown import extract_markdown_images


def split_image_nodes(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if not images:
            new_nodes.append(node)
            continue

        text = node.text

        parts = []
        for image in images:
            image_alt = image[0]
            image_link = image[1]
            image_string = f"![{image_alt}]({image_link})"
            split_parts = text.split(image_string, 1)
            if split_parts[0]:
                parts.append(TextNode(split_parts[0], TextType.TEXT))
            parts.append(
                TextNode(text=image_alt, text_type=TextType.IMAGE, url=image_link)
            )

            text = split_parts[1] if len(split_parts) > 1 else ""

        if text:
            parts.append(TextNode(text, TextType.TEXT))

        new_nodes.extend(parts)

    return new_nodes
