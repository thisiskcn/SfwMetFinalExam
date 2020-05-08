"""python script to measure coverage of the function round"""
import unittest
from roundfunc import my_round


class TestingMathFunction(unittest.TestCase):
    """Round test class"""

    def test_correct_param(self):
        """Testing Round function with valid input"""
        number_sample = 5.67
        expected_number = 6
        self.assertEqual(my_round(number_sample), expected_number)

    def test_missing_param(self):
        """Testing round function with missing parameters"""
        with self.assertRaises(TypeError):
            self.assertEqual(my_round(), True)


def test_wrong_param(self):
    """Testing round function with wrong parameters"""
    with self.assertRaises(TypeError) as err:
        my_round({})

        with self.assertRaises(TypeError) as err:
            my_round([])


if __name__ == '__main__':
    unittest.main()
