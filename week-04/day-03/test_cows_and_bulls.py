import unittest
from cows_and_bulls import CowsAndBulls 

class TestCowsAndBulls(unittest.TestCase):
    def test_CAB_constructor(self):
        cab = CowsAndBulls()
        self.assertIn(cab.number, range(1000, 10000))
        self.assertEqual(cab.state, '')
        self.assertEqual(cab.counter, 0)

    def test_guess(self):
        cab = CowsAndBulls()
        self.assertEqual(cab.guess(), '')


if __name__ == '__main__':
    unittest.main()