#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parse daily Tokyo stock prices.
"""

import csv  # import standard "csv" module

from pyschool.cmdline import parse_args


class StockPrice(object):

    def __init__(self, day, price_begin, price_max, price_min, price_end):
        self.day = day
        self.price_begin = float(price_begin)
        self.price_max = float(price_max)
        self.price_min = float(price_min)
        self.price_end = float(price_end)

    def diff(self):
        return self.price_end - self.price_begin


def process(args):
    """Parse daily Tokyo stock prices, and calculate up/down.
    """
    with open(args.filename[0]) as fp:
        reader = csv.reader(fp)  # Instantiate CSV reader with file pointer.
        for t in reader:
            p = StockPrice(*t)
            diff = p.diff()
            if diff > 0:
                message = 'up'
            elif diff < 0:
                message = 'down'
            else:
                message = 'same'
            # Write out day, up/down/same, and diff.
            print('{}\t{:5}\t{}'.format(p.day, message, round(diff, 2)))


def main():
    args = parse_args()
    process(args)


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
