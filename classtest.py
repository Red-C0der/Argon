# -*- coding: utf-8 -*-
__author__ = 'Red_C0der'

import unittest


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
    return n+1

class CheckCalc(unittest.TestCase):

    def test_calc(self):
        for i in range(5):
            self.assertEqual(calc(2), 3)
            self.assertEqual(calc(14), 15)
            self.assertEqual(calc(544), 545)
            #self.assertEqual(calc(4), 6)

if __name__ == "__main__":
    unittest.main()