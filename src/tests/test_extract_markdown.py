import unittest
from converters.extract_markdown import (
        extract_markdown_images,
        extract_markdown_links
        )

class TestExtractMarkdownImages(unittest.TestCase):
    def test_should_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_should_handle_empty_text(self):
        text = ""
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_should_handle_text_without_images(self):
        text = "This is just plain text with [a link](https://example.com)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [])

    def test_should_handle_malformed_images(self):
        text = "Broken images: ![missing paren](https://example.com ![no alt]"
        images = extract_markdown_images(text)
        self.assertEqual(images, [])


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_should_extract_links(self):
        text = "This is text with a link [to google](https://www.google.com) and [to youtube](https://www.youtube.com/)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("to google", "https://www.google.com"), ("to youtube", "https://www.youtube.com/")])

    def test_should_handle_empty_text(self):
        text = ""
        links = extract_markdown_links(text)
        self.assertEqual(links, [])

    def test_should_handle_text_without_links(self):
        text = "This is just plain text with ![an image](https://example.com)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [])

    def test_should_not_extract_image_links(self):
        text = "![image](https://example.com/img.jpg) [link](https://example.com)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("link", "https://example.com")])

    def test_should_handle_multiple_links_on_same_line(self):
        text = "[link1](url1)[link2](url2)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("link1", "url1"), ("link2", "url2")])
