import unittest
from toth_bandi_work import MyClass 

class TestTothBandi(unittest.TestCase):
    def test_apple(self):
        apple = Apple()
        self.assertEquals(apple.get_apple(), 'quince')

if __name__ == '__main__':
    unittest.main()