import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
        node2 = HTMLNode()
        self.assertEqual(node2.props_to_html(), "")

    def test_leaf(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        node3 = LeafNode(None, "This is a raw line")
        self.assertEqual(node3.to_html(), "This is a raw line")
        self.assertRaises(ValueError, lambda : LeafNode(None, None))

    def test_parent(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


if __name__ == "__main__":
    unittest.main()