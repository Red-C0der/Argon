# -*- coding: utf-8 -*-
import unittest
__author__ = 'Red_C0der'


class Decide:

    def __init__(self):
        self.history = []

    def loop(self):
        while True:
            inp = raw_input("=> ")


class Test(unittest.TestCase):

    def testDecide(self):
        pass


def calc(n):
    """
    Calculate n+1
    """
    return n+1


class CheckCalc(unittest.TestCase):

    def test_calc_small(self):
            self.assertEqual(calc(2), 3)
            self.assertEqual(calc(14), 15)
            self.assertEqual(calc(34), 35)
            self.assertEqual(calc(87), 88)
#           self.assertEqual(calc(4), 6)

    def test_calc_big(self):
        self.assertEqual(calc(100), 101)
        self.assertEqual(calc(362), 363)
        self.assertEqual(calc(2715), 2716)
        self.assertEqual(calc(291616), 291617)

if __name__ == "__main__":
    unittest.main()
