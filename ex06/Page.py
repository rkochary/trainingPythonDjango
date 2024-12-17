from elem import Elem, Text
from elements import *

class Page:
    def __init__(self, elem):
        self.elem = elem

    def __str__(self):
        doctype = "<!DOCTYPE html>\n" if isinstance(self.elem, Html) else ""
        return doctype + str(self.elem)

    def __validate(self, elem, errors):
        if not isinstance(elem, (Elem, Text)):
            errors.append(f"Invalid element type: {type(elem)}")
            return False
        if isinstance(elem, Text):
            return True
        tag = elem.tag
        children = elem.content
        if tag not in {'html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br'}:
            errors.append(f"Unknown tag: {tag}")
            return False
        if tag == 'html':
            if len(children) != 2 or not isinstance(children[0], Head) or not isinstance(children[1], Body):
                errors.append("Invalid structure in <html>: Must contain <head> and <body>")
                return False
        if tag == 'head':
            titles = [child for child in children if isinstance(child, Title)]
            if len(titles) != 1:
                errors.append("Invalid number of <title> elements in <head>")
                return False
        if tag in {'body', 'div'}:
            if not all(isinstance(child, (H1, H2, Div, Table, Ul, Ol, Span, Text, Img)) for child in children):
                errors.append(f"Invalid children in <{tag}>: Must be H1, H2, Div, Table, Ul, Ol, Span, Text, or Img")
                return False
        if tag in {'title', 'h1', 'h2', 'li', 'th', 'td'}:
            if len(children) != 1 or not isinstance(children[0], Text):
                errors.append(f"Invalid children in <{tag}>: Must contain exactly one Text element")
                return False
        if tag == 'p':
            if not all(isinstance(child, Text) for child in children):
                errors.append("Invalid children in <p>: All children must be Text elements")
                return False
        if tag == 'span':
            if not all(isinstance(child, (Text, P)) for child in children):
                errors.append("Invalid children in <span>: Must be Text or P elements")
                return False
        if tag in {'ul', 'ol'}:
            if not children or not all(isinstance(child, Li) for child in children):
                errors.append(f"Invalid children in <{tag}>: Must contain only Li elements")
                return False
        if tag == 'tr':
            ths = [child for child in children if isinstance(child, Th)]
            tds = [child for child in children if isinstance(child, Td)]
            if not children or (ths and tds):
                errors.append("Invalid structure in <tr>: Cannot mix <th> and <td> elements")
                return False
        if tag == 'table':
            if not children or not all(isinstance(child, Tr) for child in children):
                errors.append("Invalid children in <table>: Must contain only Tr elements")
                return False
        for child in children:
            if not self.__validate(child, errors):
                return False
        return True


    def is_valid(self):
        errors = []
        is_valid = self.__validate(self.elem, errors)
        if not is_valid:
            self.validation_errors = errors
        return is_valid
    
    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

def page():
    text = Text('Kikou les zouzous')
    html = Html([
        Head([
            Title([text])
        ]),
        Body([
            H1([text]),
            Img(attr={'src': 'kikou.jpg', 'alt': text})
        ])
    ])
    page = Page(html)
    if page.is_valid():
        page.write_to_file('Page.html')
        print("HTML is valid and written to file.")
    else:
        print("HTML is invalid.")
        for error in page.validation_errors:
            print(f"Error: {error}")

if __name__ == '__main__':
    page()