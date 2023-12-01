import unittest
from validation import is_valid_expression

class FactorialTest(unittest.TestCase):
    def test_is_valid_expression(self):
        self.assertTrue(is_valid_expression("1 !"))
        self.assertFalse(is_valid_expression("1 1 !"))
        self.assertFalse(is_valid_expression("! 1"))
        self.assertFalse(is_valid_expression("-1 !"))

    def test_factorial_result(self):
        self.assertEqual(#insert function name , result)


if __name__ == '__main__':
    unittest.main()
