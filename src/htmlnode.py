class HTMLNODE:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("child class should override")
    
    def props_to_html(self):
        output = ""
        if self.props == None:
            return ""
        for prop in self.props:
            output += f' {prop}="{self.props[prop]}"'
        return output
    
    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}"
    
class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.props = props
        self.tag = tag
        self.value = value

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf nodes require a value")
        if self.tag == None:
            return self.value
        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Props: {self.props}"