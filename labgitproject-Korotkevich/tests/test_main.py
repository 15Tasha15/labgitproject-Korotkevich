# test_main.py
import unittest
from src.main import *

class TestMain(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

import unittest
from src.utils import add_numbers, multiply_numbers

class TestUtils(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 1), -1)
        self.assertEqual(multiply_numbers(0, 5), 0)

if __name__ == '__main__':
    unittest.main()