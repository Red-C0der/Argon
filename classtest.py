# -*- coding: utf-8 -*-
__author__ = 'Red_C0der'

import unittest, mock

def calc(n):
    return n+1


class CheckCalc(unittest.TestCase):

    def test_calc(self):
        for i in range(5):
            self.assertEqual(calc(2), 3)

if __name__ == "__main__":
    unittest.main()