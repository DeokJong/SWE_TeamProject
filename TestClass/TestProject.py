"""
기초 연산 3가지 경우와 이스터에그, 연산자를 얻은 함수 테스트
"""

import unittest
from etc.Validation import is_valid_expression, getOperator
from etc.Easteregg_function import easterEgg_function


class ProjectTest(unittest.TestCase):
    def test_is_valid_expression(self):
        self.assertFalse(is_valid_expression("1", "="))
        self.assertFalse(is_valid_expression("-1", "="))
        self.assertFalse(is_valid_expression("1 1", "="))
        self.assertFalse(is_valid_expression("-1 -1", "="))
        self.assertFalse(is_valid_expression("1 -1", "="))
        self.assertFalse(is_valid_expression("-1 1", "="))
        self.assertFalse(is_valid_expression("1 1 1", "="))
        self.assertFalse(is_valid_expression("-1 -1 -1", "="))
        self.assertFalse(is_valid_expression("1 1 -1", "="))
        self.assertFalse(is_valid_expression("1 -1 1", "="))
        self.assertFalse(is_valid_expression("-1 1 1", "="))
        self.assertFalse(is_valid_expression("1 -1 -1", "="))
        self.assertFalse(is_valid_expression("-1 1 -1", "="))
        self.assertFalse(is_valid_expression("-1 -1 1", "="))
        self.assertFalse(is_valid_expression("- 1", "="))
        self.assertFalse(is_valid_expression("1 -", "="))
        self.assertFalse(is_valid_expression("+ -1", "="))
        self.assertFalse(is_valid_expression("-1 +", "="))
        self.assertFalse(is_valid_expression("1 1 +", "="))
        self.assertFalse(is_valid_expression("-1 -1 +", "="))
        self.assertFalse(is_valid_expression("1 -1 +", "="))
        self.assertFalse(is_valid_expression("-1 1 +", "="))
        self.assertFalse(is_valid_expression("+", "="))
        self.assertFalse(is_valid_expression("+ +", "="))
        self.assertFalse(is_valid_expression("+ + +", "="))
        self.assertTrue(is_valid_expression("1 + 1", "="))
        self.assertTrue(is_valid_expression("-1 + -1", "="))
        self.assertTrue(is_valid_expression("1 + -1", "="))
        self.assertTrue(is_valid_expression("-1 + 1", "="))

    def test_easterEgg_function(self):
        self.assertTrue(easterEgg_function("7503"))
        self.assertTrue(easterEgg_function("1015"))
        self.assertFalse(easterEgg_function("12345678912345678123456987"))

    def test_getOperator_Add(self):
        self.assertEqual(getOperator("1 + 2"), "+")
        self.assertEqual(getOperator("-1 + -2"), "+")
        self.assertEqual(getOperator("-1 + 2"), "+")
        self.assertEqual(getOperator("1 + -1"), "+")

    def test_getOperator_Sub(self):
        self.assertEqual(getOperator("1 - 2"), "-")
        self.assertEqual(getOperator("-1 - -2"), "-")
        self.assertEqual(getOperator("-1 - 2"), "-")
        self.assertEqual(getOperator("1 - -1"), "-")

    def test_getOperator_Mul(self):
        self.assertEqual(getOperator("1 * 2"), "*")
        self.assertEqual(getOperator("-1 * -2"), "*")
        self.assertEqual(getOperator("-1 * 2"), "*")
        self.assertEqual(getOperator("1 * -1"), "*")

    def test_getOperator_Fact(self):
        self.assertEqual(getOperator("1 !"), "!")
        self.assertEqual(getOperator("10 !"), "!")
        self.assertEqual(getOperator("90 !"), "!")
        self.assertEqual(getOperator("1000 !"), "!")
