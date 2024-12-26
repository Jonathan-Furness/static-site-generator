from textnode import TextType, TextNode

def main():
    node = TextNode(
            "This is a text node",
            TextType.BOLD,
            "https://www.google.com"
            )
    print(node)


if __name__ == "__main__":
    main()
