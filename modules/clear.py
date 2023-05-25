'''
Classes and functions for clear text.
'''

class ClearText:
    '''
    Clear text from HTML entities and all special characters.
    '''
    content = ""
    _temp_str = ""
    _final_result = ""
    _separator = ""
    def __init__(self, content, separator=" "):
        self.content = content
        self._separator = separator

    def _remove_special_entities(self):
        is_entity = False
        entity = ""
        for char in self.content: # it analyses char by char of string
            if char == "&":
                if not is_entity:
                    is_entity = True
                    entity += char
                    self._temp_str += self._separator
                else:
                    is_entity = False
                    self._temp_str += char
            elif char == ";":
                if is_entity:
                    is_entity = False
                else:
                    self._temp_str += char
            else:
                if is_entity:
                    if not char.isalnum():
                        is_entity = False
                        self._temp_str += self._separator + entity
                        entity = ""
                    else:
                        entity += entity + char
                        entity = ""
                else:
                    self._temp_str += char
                    entity = ""
        if is_entity:
            self._temp_str += entity

    def _remove_special_chars(self):
        for char in self._temp_str:
            if char.isalnum():
                self._final_result += char
            else:
                self._final_result += self._separator


    def get_clear_text(self):
        '''
        Returns clear text without HTML entities and special characters.
        '''
        self._remove_special_entities()
        self._remove_special_chars()
        return self._final_result

