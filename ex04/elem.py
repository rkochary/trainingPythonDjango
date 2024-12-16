# #!/usr/bin/python3


# class Text(str):
#     """
#     A Text class to represent a text you could use with your HTML elements.

#     Because directly using str class was too mainstream.
#     """

#     def __str__(self):
#         """
#         Do you really need a comment to understand this method?..
#         """
#         return super().__str__().replace('\n', '\n<br />\n')


# class Elem:
#     """
#     Elem will permit us to represent our HTML elements.
#     """
#     [...]

#     def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
#         """
#         __init__() method.

#         Obviously.
#         """
#         [...]

#     def __str__(self):
#         """
#         The __str__() method will permit us to make a plain HTML representation
#         of our elements.
#         Make sure it renders everything (tag, attributes, embedded
#         elements...).
#         """
#         if self.tag_type == 'double':
#             [...]
#         elif self.tag_type == 'simple':
#             [...]
#         return result

#     def __make_attr(self):
#         """
#         Here is a function to render our elements attributes.
#         """
#         result = ''
#         for pair in sorted(self.attr.items()):
#             result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
#         return result

#     def __make_content(self):
#         """
#         Here is a method to render the content, including embedded elements.
#         """

#         if len(self.content) == 0:
#             return ''
#         result = '\n'
#         for elem in self.content:
#             result += [...]
#         return result

#     def add_content(self, content):
#         if not Elem.check_type(content):
#             raise Elem.ValidationError
#         if type(content) == list:
#             self.content += [elem for elem in content if elem != Text('')]
#         elif content != Text(''):
#             self.content.append(content)

#     @staticmethod
#     def check_type(content):
#         """
#         Is this object a HTML-compatible Text instance or a Elem, or even a
#         list of both?
#         """
#         return (isinstance(content, Elem) or type(content) == Text or
#                 (type(content) == list and all([type(elem) == Text or
#                                                 isinstance(elem, Elem)
#                                                 for elem in content])))


# if __name__ == '__main__':
#     [...]


#!/usr/bin/python3
class Text(str):
    def __str__(self):
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')

class Elem:
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = []
        if not (self.check_type(content) or content is None):
            raise self.ValidationError("Invalid content type")
        if content is not None:
            self.add_content(content)
        if tag_type not in ['double', 'simple']:
            raise self.ValidationError("Invalid tag type")
        self.tag_type = tag_type

    def __str__(self):
        attr_str = self.__make_attr()
        if self.tag_type == 'double':
            return f"<{self.tag}{attr_str}>{self.__make_content()}</{self.tag}>"
        elif self.tag_type == 'simple':
            return f"<{self.tag}{attr_str} />"

    def __make_attr(self):
        return ''.join(f' {key}="{value}"' for key, value in sorted(self.attr.items()))

    def __make_content(self):
        if not self.content:
            return ''
        result = []
        for elem in self.content:
            elem_str = str(elem)
            if elem_str.strip():
                indented_elem_str = '\n  '.join(elem_str.split('\n'))
                result.append(f"\n  {indented_elem_str}")
        content = ''.join(result)
        return content + '\n' if content else ''

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError("Invalid content type")
        if isinstance(content, list):
            self.content.extend(elem for elem in content if elem != Text(''))
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

def elem():
    text = Text('"Kikou les zouzous"')
    elem = Elem(tag='html', attr={}, content=[
        Elem(tag='head', attr={}, content=[
            Elem(tag='title', attr={}, content=[text])
        ]),
        Elem(tag='body', attr={}, content=[
            Elem(tag='h1', attr={}, content=[text]),
            Elem(tag='img', attr={'src': 'kikou.jpg', 'alt': text}, tag_type='simple')
        ])
    ])
    print(elem)

if __name__ == '__main__':
    elem()

