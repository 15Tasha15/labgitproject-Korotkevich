# test_main.py
import unittest
from src.main import *

class TestMain(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()