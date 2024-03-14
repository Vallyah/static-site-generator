class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        result = ""
        if self.props:
            for key, value in self.props.items():
                result += f" {key}=\"{value}\""
        return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        if (value == None):
            raise ValueError("Invalid HTML: no value")
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        if (tag == None):
            raise ValueError("Invalid HTML: no tag")
        if (children == None or len(children) == 0):
            raise ValueError("Invalid HTML: no children")
        super().__init__(tag, None, children, props)

    def to_html(self):
        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
