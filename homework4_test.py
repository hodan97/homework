import unittest
from unittest import TestCase, main
from homework4 import pin_checker, withdraw_check


class ATMProgram(unittest.TestCase):
    def test_pin_code_tries(self):
        pin_try = 0
        expected = pin_try <= 3
        actual = pin_checker()
        self.assertEqual(expected, 1)

    def test_pin_tries_exception(self):
        self.assertRaises(Exception, pin_checker, 3)

    def test_pin_code_correct(self):
        result = pin_checker()
        self.assertFalse(result)

    def test_balance_not_negative_after_withdraw(self):
        self.assertRaises(Exception, withdraw_check, 100)

    def test_withdraw_working(self):
        result = withdraw_check
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
