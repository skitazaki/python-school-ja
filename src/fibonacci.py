#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n):
    assert type(n) == int
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    for i in range(13):
        print("{:2}\t--fib-->\t{:3}".format(i, fib(i)))

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
