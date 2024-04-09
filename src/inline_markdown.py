from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        remaining_text = old_node.text
        for image_tup in extract_markdown_images(old_node.text):
            split_text = remaining_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)

            if len(split_text[0]) > 0:
                new_nodes.append(TextNode(split_text[0], text_type_text))
            
            new_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))

            remaining_text = split_text[1]
        
        if len(remaining_text) > 0:
            new_nodes.append(TextNode(remaining_text, text_type_text))
    
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        remaining_text = old_node.text
        for link_tup in extract_markdown_links(old_node.text):
            split_text = remaining_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)

            if len(split_text[0]) > 0:
                new_nodes.append(TextNode(split_text[0], text_type_text))
            
            new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))

            remaining_text = split_text[1]
        
        if len(remaining_text) > 0:
            new_nodes.append(TextNode(remaining_text, text_type_text))
    
    return new_nodes
