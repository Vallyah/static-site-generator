import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", text_type_bold, None)
        self.assertEqual(node, node3)

        node = TextNode("This is a text node", text_type_bold, "http://127.0.0.1")
        node2 = TextNode("This is a text node", text_type_bold, "http://127.0.0.1")
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node, node2)
        
        node3 = TextNode("This is another text node", text_type_bold, None)
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is a text node", text_type_bold, "http://127.0.0.1")
        self.assertNotEqual(node, node4)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is another text node", text_type_italic, "http://127.0.0.1")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")
        self.assertEqual(repr(node2), "TextNode(This is another text node, italic, http://127.0.0.1)")

if __name__ == "__main__":
    unittest.main()
