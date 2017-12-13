import unittest
from sharpie import Sharpie

class TestSharpie(unittest.TestCase):
    def test_use(self):
        pen = Sharpie('red', 0.7)
        original_ink = pen.ink_amount
        self.assertLess(pen.use(), original_ink)

if __name__ == '__main__':
    unittest.main()
