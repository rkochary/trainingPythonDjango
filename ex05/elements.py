from elem import Elem, Text

# Base HTML element classes derived from Elem
class Html(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('html', attr or {}, content)

class Head(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('head', attr or {}, content)

class Body(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('body', attr or {}, content)

class Title(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('title', attr or {}, content)

class Meta(Elem):
    def __init__(self, attr=None):
        super().__init__('meta', attr or {}, None, 'simple')

class Img(Elem):
    def __init__(self, attr=None):
        super().__init__('img', attr or {}, None, 'simple')

class Table(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('table', attr or {}, content)

class Th(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('th', attr or {}, content)

class Tr(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('tr', attr or {}, content)

class Td(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('td', attr or {}, content)

class Ul(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('ul', attr or {}, content)

class Ol(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('ol', attr or {}, content)

class Li(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('li', attr or {}, content)

class H1(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('h1', attr or {}, content)

class H2(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('h2', attr or {}, content)

class P(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('p', attr or {}, content)

class Div(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('div', attr or {}, content)

class Span(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__('span', attr or {}, content)

class Hr(Elem):
    def __init__(self, attr=None):
        super().__init__('hr', attr or {}, None, 'simple')

class Br(Elem):
    def __init__(self, attr=None):
        super().__init__('br', attr or {}, None, 'simple')


def elements():
    text = Text('Hello ground!')
    html = Html([
        Head([
            Title([text])
        ]),
        Body([
            H1([text]),
            Img(attr={'src': '"http://i.imgur.com/pfp3T.jpg'})
        ])
    ])
    print(html)

if __name__ == '__main__':
    elements()
