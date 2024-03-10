class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        result = ""
        if self.props:
            for key, value in self.props.items():
                result += f" {key}=\"{value}\""
        return result

    def __repr__(self):
        str_list = ["\"HTMLNode\": {"]
        str_list.append(f"\"tag\": \"{self.tag}\",")
        str_list.append(f"\"value\": \"{self.value}\",")
        str_list.append("\"children\": {")
        if self.children:
            for child in self.children:
                str_list.append(child.__repr__() + ",")
        str_list.append("},")
        str_list.append("\"props\": {")
        if self.props:
            for key, value in self.props.items():
                str_list.append(f"\"{key}\": \"{value}\"")
        str_list.append("},")
        str_list.append("}")
        return "\n".join(str_list)
