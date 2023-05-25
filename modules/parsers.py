'''
Contains class, which removes HTML, CSS and JS content from HTML pages.
'''

class RemoveHTMLCode:
    '''
    This class is responsible for removing HTML tags and CSS/JS content from given string.

    Data is given in constructor e.g.:
    c = RemoveHTMLCode(content: str)

    For get cleared string, just run:
    c.get_text() : str
    '''
    content = ""
    parts = []
    _tmp_part = ""
    _in_tag = ""
    result = ""

    def __init__(self, content):
        self.content = content
        self.parts = []
        self._tmp_part = ""
        self._in_tag = ""

    def _add_tmp_part(self):
        '''
        Adds temporary part to list of parts of content.
        '''
        if len(self._tmp_part) > 0:
            self.parts.append(self._tmp_part)
            self._tmp_part = ""

    def _add_last_tag_content(self):
        '''
        Adds Tag content to parts (when tag has no ">" ending character)
        '''
        if len(self._in_tag) > 0:
            self.parts.append(self._in_tag)

    def _divide_to_parts(self):
        '''
        Removes HTML tags and JS/CSS code.
        Produces parts of text in list.
        '''
        # conditional variables used in for loop:
        is_tag = False # its changed to True when tag starts and to False when it ends
        quote = None # if text is quoted, this contains quotation char
        code = None #  if char is in code, this contains expected ending tag
        code_quote = None # its used to know if char is in quote inside code or not
        clear_tag = False # determines if current tag should be cleared
        for char in self.content:
            if char == "<": # this char can start tag
                if not quote: 
                    if not code_quote:
                        self._add_tmp_part()
                        is_tag = True
                if not code_quote:
                    self._in_tag += char
            elif char == ">": # this char can end tag
                if is_tag:
                    if not quote:
                        is_tag = False
                        clear_tag = True
                    self._in_tag += char
                    if not code: # checks if this tag starts script or style
                        if self._in_tag.lower().startswith('<script'):
                            code = "</script"
                        if self._in_tag.lower().startswith('<style'):
                            code = "</style"
                    else:
                        if self._in_tag.lower().startswith(code):
                            code = None
                    if clear_tag:
                        self._in_tag = ""
                        clear_tag = False
                else:
                    if not code:
                        self._tmp_part += char
            elif is_tag: # this part is important when char is inside tag and it's not '<' or '>'
                # this part is responsible for determining quotes in tags
                if not quote:
                    if char in ("'", '"'):
                        quote = char
                else: # it must be quoted
                    if char == quote: # quote ends here
                        quote = None
                self._in_tag += char
            elif not is_tag:
                if code:
                    # this part is responsible for determining code quotes
                    if char in ("'", '"'):
                        if code_quote:
                            code_quote = None
                        else:
                            code_quote = char

                if not code:
                    self._tmp_part += char # adds char to temporary part
        # add cached data to "parts"
        self._add_tmp_part() 
        # if last part starts with < but we can't find >, it's worth to take it.
        if is_tag:
            # this is executed when tag was not ended but content was,
            # which means it's not HTML tag.
            self._add_last_tag_content()

    def _concat_parts(self):
        '''
        Build string from parts.
        '''
        self.result = " ".join(self.parts)

    def get_text(self):
        '''
        Returns text without HTML tags, CSS and JavaScript code.
        '''
        self._divide_to_parts()
        self._concat_parts()
        self.parts = []
        self._tmp_part = ""
        return self.result
    