import string

class MyClass():
    def get_apple(self):
        return 'quince'

    def summa(self, numbers = []):
        summa = 0
        for number in numbers:
            summa += number
        return summa

    def string_processor(self, my_string):
        my_string = my_string.lower()
        chars = {}
        for char in my_string:
            if char not in string.whitespace:
                if char not in list(chars.keys()):
                    chars[char] = 1
                else:
                    chars[char] += 1
        return chars

    def is_anagram(self, string1 = '', string2 = ''):
        chars1 = self.string_processor(string1)
        chars2 = self.string_processor(string2)
        return chars1 == chars2