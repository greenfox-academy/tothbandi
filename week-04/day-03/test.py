import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(2, 3), 5)

    def test_add_nothing(self):
        self.assertEqual(extend.add(), 0)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(4, 1), 5)

    def test_max_of_three_first_case(self):
        self.assertEqual(extend.max_of_three(5, 4, 3), 5)

    def test_max_of_three_second_case(self):
        self.assertEqual(extend.max_of_three(4, 3, 5), 5)

    def test_max_of_three_fourth_case(self):
        self.assertEqual(extend.max_of_three(3, 4, 5), 5)
    
    def test_max_of_three_third_case(self):
        self.assertEqual(extend.max_of_three(3, 5, 4), 5)

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,5]), 5)

    def test_median_four_twoandhalf(self):
        self.assertEqual(extend.median([4,3,2,1]), 2)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5]), 3)

    def test_median_five_one(self):
        self.assertEqual(extend.median([1,1,2,2,1]), 1)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))
    
    def test_is_vovel_b(self):
        self.assertFalse(extend.is_vovel('b'))

    def test_is_vovel__(self):
        self.assertFalse(extend.is_vovel(' '))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

    def test_translate_ember(self):
        self.assertEqual(extend.translate('ember'), 'evembever')
    

if __name__ == '__main__':
    unittest.main()