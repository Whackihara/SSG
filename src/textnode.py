from enum import Enum

class TextType(Enum):
        NORMAL = "{1}"
        BOLD = "**{1}**"
        ITALIC = "*{1}*"
        CODE = "```{1}```"
        LINK = "[link]({1})"
        IMAGE = "![{1}]({2})"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, textnode):
         return (self.text == textnode.text and
            self.text_type == textnode.text_type and
            self.url == textnode.url)
    def __repr__(self):
         return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

        