#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parse daily Tokyo stock prices.
"""

import csv  # import standard "csv" module

from pyschool.cmdline import parse_args


class StockPrice(object):

    def __init__(self, day, price_end, price_begin, price_max, price_min):
        self.day = day
        self.price_end = float(price_end)
        self.price_begin = float(price_begin)
        self.price_max = float(price_max)
        self.price_min = float(price_min)

    def diff(self):
        return self.price_end - self.price_begin


def process(args):
    """Parse daily Tokyo stock prices, and calculate up/down.
    """
    with open(args.filename[0], encoding=args.encoding) as fp:
        reader = csv.reader(fp)  # Instantiate CSV reader with file pointer.
        _ = next(reader)  # skip header line
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
            print(f'{p.day}\t{message:5}\t{round(diff, 2)}')


def main():
    args = parse_args()
    process(args)


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
