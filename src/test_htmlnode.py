import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
        node2 = HTMLNode()
        self.assertEqual(node2.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()