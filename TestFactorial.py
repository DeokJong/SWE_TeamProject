import unittest
from Factorial import factorial
from validation import is_valid_expression


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial("1 !"), 1)
        self.assertEqual(factorial("3 !"), 6)
        self.assertEqual(factorial("10 !"), 3628800)

    def test_is_valid_expression_for_factorial_symbol(self):
        self.assertTrue(is_valid_expression("3 !"))
        self.assertFalse(is_valid_expression("! !"))
        self.assertFalse(is_valid_expression("3 3 !"))
        self.assertFalse(is_valid_expression("! 3"))


if __name__ == '__main__':
    unittest.main()
