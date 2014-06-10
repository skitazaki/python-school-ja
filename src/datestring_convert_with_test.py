#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


def datestring_convert(s):
    """Convert datetime string which appears in subversion commit log.

    >>> TEST_1 = "2012-01-14 07:56:02"
    >>> TEST_2 = "2012-01-14 04:46:30 +0900"
    >>> d1 = datestring_convert(TEST_1)
    >>> d2 = datestring_convert(TEST_2)
    >>> diff = d1 - d2
    >>> print("{} ==> {}".format(TEST_1, TEST_2))
    2012-01-14 07:56:02 ==> 2012-01-14 04:46:30 +0900
    >>> print("DIFF: days={}, seconds={}".format(diff.days, diff.seconds))
    DIFF: days=0, seconds=11372
    """
    assert type(s) == str, "Argument must be string"
    dt = s.split()
    year, month, day = map(int, dt[0].split("-"))
    hour, minute, second = map(int, dt[1].split(":"))
    return datetime.datetime(year, month, day, hour, minute, second)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
