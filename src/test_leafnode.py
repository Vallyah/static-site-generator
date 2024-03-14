import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        node3 = LeafNode(None, "This is a raw line")
        self.assertEqual(node3.to_html(), "This is a raw line")
        self.assertRaises(ValueError, lambda : LeafNode(None, None))


if __name__ == "__main__":
    unittest.main()