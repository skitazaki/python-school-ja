#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# Local script to test.
from fibonacci import fib


class FibonacciTest(unittest.TestCase):

    def test(self):
        self.assertEqual(0, fib(0))
        self.assertEqual(1, fib(1))
        self.assertEqual(1, fib(2))
        self.assertEqual(2, fib(3))
        self.assertEqual(3, fib(4))
        self.assertEqual(5, fib(5))
        self.assertEqual(8, fib(6))
        self.assertEqual(13, fib(7))
        self.assertEqual(21, fib(8))
        self.assertEqual(34, fib(9))
        self.assertEqual(55, fib(10))
        self.assertEqual(89, fib(11))
        self.assertEqual(144, fib(12))

    def test_invalid_argument(self):
        try:
            fib(1.0)
            self.fail("Did not raise AssertionError")
        except AssertionError:
            pass
        try:
            fib("1000")
        except AssertionError:
            pass
        else:
            self.fail("Did not raise AssertionError")

if __name__ == '__main__':
    unittest.main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
