import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node3)

        node = TextNode("This is a text node", "bold", "http://127.0.0.1")
        node2 = TextNode("This is a text node", "bold", "http://127.0.0.1")
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
        
        node3 = TextNode("This is another text node", "bold", None)
        self.assertNotEqual(node, node3)

        node4 = TextNode("This is a text node", "bold", "http://127.0.0.1")
        self.assertNotEqual(node, node4)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is another text node", "italic", "http://127.0.0.1")
        self.assertEqual(node.repr(), "TextNode(This is a text node, bold, None)")
        self.assertEqual(node2.repr(), "TextNode(This is another text node, italic, http://127.0.0.1)")


if __name__ == "__main__":
    unittest.main()
