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


if __name__ == '__main__':
    unittest.main()