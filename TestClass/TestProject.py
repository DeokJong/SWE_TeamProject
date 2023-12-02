import unittest
from etc.Validation import is_valid_expression, getOperator
from etc.Easteregg_function import easterEgg_function


class ProjectTest(unittest.TestCase):
    def test_is_valid_expression(self):
        self.assertFalse(is_valid_expression("1 +", "="))
        self.assertFalse(is_valid_expression("1 1 +", "="))
        self.assertFalse(is_valid_expression("+ 1", "="))
        self.assertFalse(is_valid_expression("-1 +", "="))

    def test_easterEgg_function(self):
        self.assertTrue(easterEgg_function("777"))
        self.assertFalse(easterEgg_function("666"))

    def test_getOperator(self):
        self.assertEqual(getOperator("1 + 2"), "+")
        self.assertEqual(getOperator("1 - 2"), "-")
        self.assertEqual(getOperator("1 * 2"), "*")
        self.assertEqual(getOperator("1 !"), "!")


if __name__ == '__main__':
    unittest.main()
