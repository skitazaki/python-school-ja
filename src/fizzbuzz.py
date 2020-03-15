#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Toy FizzBuzz implementation.
"""

import argparse

SEPARATOR = "=" * 78


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int)
    args = parser.parse_args()
    if args.number <= 0:
        parser.error("Number must be positive: {}".format(args.number))
    return args.number


def fizzbuzz(i):
    """Basic implementation."""
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 5 == 0:
        return "Buzz"
    elif i % 3 == 0:
        return "Fizz"
    else:
        return i


def fizzbuzz_iter(n):
    """Generator, using `zip` and postposition IF statement."""
    fb = ("Fizz", "Buzz")
    i = 1
    while i <= n:
        t = (i % 3 == 0, i % 5 == 0)
        s = ''.join(map(lambda t: t[1], filter(lambda t: t[0], zip(t, fb))))
        yield s if s else i
        i += 1


def fizzbuzz_list(n):
    """`map` and `lambda` functions, showing usages of `enumerate`, `type`, and `zip`."""
    ret = []
    m = range(1, n + 1)
    m1 = map(lambda i: i if i % 3 > 0 else "Fizz", m)
    m2 = map(lambda i: i if i % 5 > 0 else "Buzz", m)
    m3 = map(lambda i: i if i % 15 > 0 else "FizzBuzz", m)
    for i, t in enumerate(zip(m1, m2, m3)):
        r = [i for i in t if type(i) == str]
        ret.append(list(r).pop() if r else str(i + 1))
    return ret


def main():
    n = parse_args()

    print(SEPARATOR)
    for i in range(1, n + 1):
        val = fizzbuzz(i)
        print(val)

    print(SEPARATOR)
    for i in fizzbuzz_iter(n):
        print(i)

    print(SEPARATOR)
    print('\n'.join(fizzbuzz_list(n)))


def test():
    expected = [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
        "16"
    ]
    actual = fizzbuzz_list(16)
    assert len(expected) == len(actual)
    for e, a in zip(expected, actual):
        assert e == a, 'expected={}, actual={}'.format(e, a)

if __name__ == "__main__":
    main()
    #test()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
