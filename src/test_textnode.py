import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.example.com")
        self.assertEqual(node.url, "https://www.example.com")

    def test_text_type_eq(self):
        self.assertEqual(TextType.BOLD, TextType.BOLD)
    
    def test_text_type_ne(self):
        self.assertNotEqual(TextType.BOLD, TextType.ITALIC)

if __name__ == "__main__":
    unittest.main()