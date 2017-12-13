import unittest
from toth_bandi_work import MyClass 

class TestTothBandi(unittest.TestCase):
    def test_apple(self):
        apple = MyClass()
        self.assertEqual(apple.get_apple(), 'quince')

    def test_sum_of_list_of_numbers(self):
        sum_of_list = MyClass()
        self.assertEqual(sum_of_list.summa([3, 4, 5]), 12)

    def test_sum_of_empty_list(self):
        sum_of_list = MyClass()
        self.assertEqual(sum_of_list.summa([]), 0)

    def test_sum_of_one_element_list(self):
        sum_of_list = MyClass()
        self.assertEqual(sum_of_list.summa([5]), 5)    

    def test_sum_of_null(self):
        sum_of_list = MyClass()
        self.assertEqual(sum_of_list.summa(), 0)
    
    def test_anagram(self):
        anagram = MyClass()
        self.assertEqual(anagram.is_anagram('orrszarvu', 'rovar ruzs'), True)

    def test_anagram_empty_string(self):
        anagram = MyClass()
        self.assertEqual(anagram.is_anagram('', ' '), True)

    def test_anagram_null(self):
        anagram = MyClass()
        self.assertEqual(anagram.is_anagram(), True)
    
    def test_anagram_with_not_anagrams(self):
        anagram = MyClass()
        self.assertEqual(anagram.is_anagram('ok', 'nok'), False)

    def test_anagram_no_case_sensitive(self):
        anagram = MyClass()
        self.assertEqual(anagram.is_anagram('Orrszarvu', 'rovar ruzs'), True)           
        


if __name__ == '__main__':
    unittest.main()