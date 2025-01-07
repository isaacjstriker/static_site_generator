import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node, node2)

    def test_ne(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph", children=[HTMLNode("b", "Bold")])
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", "This is a paragraph", props={"class": "paragraph"})
        self.assertEqual(node.props_to_html(), 'class="paragraph"')

    def test_props_to_html_none(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph", props={"class": "paragraph"})
        self.assertEqual(repr(node), '<p class="paragraph">')

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("b", "Bold")
        self.assertEqual(node.to_html(), "<b>Bold</b>")

    def test_to_html_no_value(self):
        node = LeafNode("b", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Bold")
        self.assertEqual(node.to_html(), "Bold")

    def test_eq(self):
        node = LeafNode("b", "Bold")
        node2 = LeafNode("b", "Bold")
        self.assertEqual(node, node2)

    def test_ne(self):
        node = LeafNode("b", "Bold")
        node2 = LeafNode("b", "Bold", props={"class": "bold"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = LeafNode("b", "Bold", props={"class": "bold"})
        self.assertEqual(node.props_to_html(), 'class="bold"')

    def test_props_to_html_none(self):
        node = LeafNode("b", "Bold")
        self.assertEqual(node.props_to_html(), "")

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph")])
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p></div>")

    def test_eq(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph")])
        node2 = ParentNode("div", [LeafNode("p", "This is a paragraph")])
        self.assertEqual(node, node2)

    def test_ne(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph")])
        node2 = ParentNode("div", [LeafNode("p", "This is a paragraph")], props={"class": "paragraph"})
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph")], props={"class": "paragraph"})
        self.assertEqual(node.props_to_html(), 'class="paragraph"')

    def test_props_to_html_none(self):
        node = ParentNode("div", [LeafNode("p", "This is a paragraph")])
        self.assertEqual(node.props_to_html(), "")
    
    def test_parent_node_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "This is a paragraph")])

    def test_parent_node_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

class TestTextToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_normal(self):
        from textnode import TextNode, TextType
        from htmlnode import LeafNode
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode(None, "This is a text node"))
    
    def test_text_node_to_html_node_bold(self):
        from textnode import TextNode, TextType
        from htmlnode import LeafNode
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("b", "This is a text node"))

    def test_text_node_to_html_node_italic(self):
        from textnode import TextNode, TextType
        from htmlnode import LeafNode
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("i", "This is a text node"))
    
    def test_text_node_to_html_node_code(self):
        from textnode import TextNode, TextType
        from htmlnode import LeafNode
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("code", "This is a text node"))
    
    def test_text_node_to_html_node_link(self):
        from textnode import TextNode, TextType
        from htmlnode import LeafNode
        node = TextNode("This is a text node", TextType.LINK, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("a", "This is a text node", props={"href": "https://www.example.com"}))
    
    def test_text_node_to_html_node_image(self):
        from textnode import TextNode, TextType
        from htmlnode import LeafNode
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("img", None, props={"src": "https://www.example.com"}))    

if __name__ == "__main__":
    unittest.main()