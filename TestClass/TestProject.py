"""
식의 유효성 검사, 이스터에그, 연산자를 얻는 함수 테스트
"""

import unittest
from etc.Validation import is_valid_expression, getOperator
from etc.Easteregg_function import easterEgg_function

class TestIsValidExpression(unittest.TestCase):
    def test_is_not_valid_expression(self):
        self.assertFalse(is_valid_expression("3 / 5", "="))
        self.assertFalse(is_valid_expression("3 +", "="))
        self.assertFalse(is_valid_expression("3 *", "="))
        self.assertFalse(is_valid_expression("3 -", "="))
        self.assertFalse(is_valid_expression("3 5", "!"))
        self.assertFalse(is_valid_expression("3 5", "="))
        self.assertFalse(is_valid_expression("+ 3", "="))

    def test_is_valid_expression(self):
        self.assertTrue(is_valid_expression("3 + 5", "="))
        self.assertTrue(is_valid_expression("3 * 5", "="))
        self.assertTrue(is_valid_expression("3 - 5", "="))
        self.assertTrue(is_valid_expression("3", "!"))

class TestEasterEgg(unittest.TestCase):
    def test_easterEgg_function(self):
        self.assertTrue(easterEgg_function("7503"))
        self.assertTrue(easterEgg_function("1015"))
    
    def test_not_easterEgg_function(self):
        self.assertFalse(easterEgg_function("123456789"))
        
class TestGetOperator(unittest.TestCase):
    def test_getOperator_Add(self):
        self.assertEqual(getOperator("3 + 5"), "+")
        self.assertEqual(getOperator("-3 + -5"), "+")
        self.assertEqual(getOperator("-3 + 5"), "+")
        self.assertEqual(getOperator("3 + -5"), "+")

    def test_getOperator_Sub(self):
        self.assertEqual(getOperator("3 - 5"), "-")
        self.assertEqual(getOperator("-3 - -5"), "-")
        self.assertEqual(getOperator("-3 - 5"), "-")
        self.assertEqual(getOperator("3 - -5"), "-")

    def test_getOperator_Mul(self):
        self.assertEqual(getOperator("3 * 5"), "*")
        self.assertEqual(getOperator("-3 * -5"), "*")
        self.assertEqual(getOperator("-3 * 3"), "*")
        self.assertEqual(getOperator("3 * -5"), "*")

    def test_getOperator_Fact(self):
        self.assertEqual(getOperator("1 !"), "!")
        self.assertEqual(getOperator("10 !"), "!")
        self.assertEqual(getOperator("90 !"), "!")
        self.assertEqual(getOperator("1000 !"), "!")
