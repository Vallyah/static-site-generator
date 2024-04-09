from textnode import (
    TextNode
)
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        print(isinstance(old_node, TextNode))
        if not isinstance(old_node, TextNode):
            new_nodes.append(old_node)
        else:
            split_text = old_node.text.split(delimiter)

            if len(split_text) % 2 != 1:
                raise Exception(f"Missing closing {delimiter} delimiter in text: {old_node.text}")
            
            use_old_type = True
            for text in split_text:
                if len(text) > 0:
                    if use_old_type:
                        new_nodes.append(TextNode(text, old_node.text_type))
                    else:
                        new_nodes.append(TextNode(text, text_type))
                use_old_type = not use_old_type
                
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches