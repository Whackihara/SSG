import unittest

from htmlnode import HTMLNODE, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        hreftargetTest = HTMLNODE(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(hreftargetTest.props_to_html(),' href="https://www.google.com" target="_blank"')
        print(hreftargetTest)
    
    def test_children(self):
        HTMLLink = HTMLNODE(tag="a", value="Searchypoop", props={"href": "https://www.google.com", "target": "_blank"})
        HTMLImage = HTMLNODE(tag="a", value="Herpderp", props={"image": "/images/derp.jpg"})
        HTMLChildren = HTMLNODE(tag="p", value="Look at this stupid link", children=(HTMLImage,HTMLLink))
        print(f"HTMLLink Props: {HTMLLink.props_to_html()}")
        print(f"HTMLImage Props: {HTMLImage.props_to_html()}")
        print(f"HTMLChildren Props: {HTMLChildren.props_to_html()}")
        print(HTMLChildren)
    
    def test_leaf(self):
        pNode = LeafNode("p", "This is a paragraph of text.")
        linkNode = LeafNode("a", "Click this shit!", props={"href": "https://www.google.com"})
        imgNode = LeafNode("img", "Nice picture of leaves?", props={"src": "images/derp.jpg"})
        print(pNode.to_html())
        print(linkNode.to_html())
        print(imgNode.to_html())

if __name__ == "__main__":
    unittest.main()