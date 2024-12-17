#!/usr/bin/python3
class Text(str):
    def __str__(self):
        escaped = super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')
        return f'"{escaped}"'


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
