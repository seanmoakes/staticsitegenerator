import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2, f"No difference\n\n{node.text}\n{node2.text}")

    def test_type_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2, f"No difference\n\n{node.text_type}\n{node2.text_type}")

    def test_url_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        self.assertNotEqual(node, node2, f"No difference\n\n{node.url}\n{node2.url}")

    def test_url_isnone(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url, 'URL should be None')

    def test_url_is_not_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        self.assertIsNotNone(node.url, 'URL should not be None')

if __name__ == "__main__":
    unittest.main()
