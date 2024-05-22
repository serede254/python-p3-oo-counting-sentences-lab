#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        self._value = value if isinstance(value, str) else ''

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        cleaned_value = re.sub(r'[.!?]+', '.', self.value)
        sentences = cleaned_value.split('.')
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
    
