"""
팩토리얼 연산에 대한 테스트케이스를 생성
이는 TDD를 위해서임
"""
import unittest
from CalculateFunction.Factorial import factorial
from etc.Validation import is_valid_expression, print_error_message


class TestFactorial(unittest.TestCase):
    # def test_factorial(self):
    #    self.assertEqual(factorial("1 !"), 1)
    #    self.assertEqual(factorial("3 !"), 6)
    #    self.assertEqual(factorial("10 !"), 3628800)

    def test_is_valid_expression_for_factorial_symbol(self):
        self.assertTrue(is_valid_expression("3 !"))
        self.assertFalse(is_valid_expression("! !"))
        self.assertFalse(is_valid_expression("3 3 !"))
        self.assertFalse(is_valid_expression("! 3"))
        self.assertFalse(is_valid_expression("-3 !"))
        self.assertFalse(is_valid_expression("! !"))
        self.assertFalse(is_valid_expression("-3 -3 !"))
        self.assertFalse(is_valid_expression("! -3"))

    def test_print_error_message(self):
        self.assertEqual(print_error_message("3 5 !"), "[ERROR] Input Error")
        self.assertEqual(print_error_message("-3 !"), "[ERROR] Out Of Range")

    def test_factorial_zero(self):
        self.assertEqual(factorial("0 !"), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial("2 !"), 2)
        self.assertEqual(factorial("3 !"), 6)
        self.assertEqual(factorial("4 !"), 24)
        self.assertEqual(factorial("5 !"), 120)
        self.assertEqual(factorial("6 !"), 720)
        self.assertEqual(factorial("30 !"), 265252859812191058636308480000000)

    def test_factorial_negative(self):
        self.assertFalse(is_valid_expression("-3 !", "!"))
        self.assertFalse(is_valid_expression("-30 !", "!"))
