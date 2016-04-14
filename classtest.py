# -*- coding: utf-8 -*-
__author__ = 'Red_C0der'

import doctest

class Test:

    def __init__(self):
        pass

    def calc(self, n):
        """
            Return N+1

            >>> calc(1)
            2
            >>> calc(5)
            6
            >>> calc(2713)
            2714
            >>> fib(0)
            1
            >>>

            """
        return n + 1

if __name__ == "__main__":
    doctest.testmod()