import unittest
import random

random.seed(20)

from dummy.main import greet, depart


class TestSimple(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("indi"), None)

    def test_depart(self):
        self.assertEqual(depart("indi"), None)

if __name__ == '__main__':
    unittest.main()