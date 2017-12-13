class MyClass():
    def get_apple(self):
        return 'quince'

    def summa(self, numbers = []):
        summa = 0
        for number in numbers:
            summa += number
        return summa

    def is_anagram(self, string1, string2):
        return True