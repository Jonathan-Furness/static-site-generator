from .htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, children = None, props = props)

    def to_html(self):
        if self.tag is None:
            return self.value
        
        
        if self.props:            
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'
