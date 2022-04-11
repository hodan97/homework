import unittest
from calculator import *

class MyTestCase(unittest.TestCase):
    def adding_test(self):
        self.assertTrue(calculator.add(4))  # add assertion here


if __name__ == '__main__':
    unittest.main()
