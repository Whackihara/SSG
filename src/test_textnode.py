import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node = TextNode("Hngasdfasdfasd", TextType.LINK, "https://www.linky.com")
        node2 = TextNode("Hngasdfasdfasd", TextType.LINK, "https://www.linky.com")
        self.assertEqual(node, node2)
        node = TextNode("NotEqual", TextType.NORMAL)
        node2 = TextNode("NotEqual", TextType.BOLD)
        self.assertNotEqual(node, node2)
        node = TextNode("HaveURL", TextType.IMAGE, "./penis.jpg")
        node2 = TextNode("HaveURL", TextType.IMAGE)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()