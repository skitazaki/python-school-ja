#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parse daily Tokyo stock prices.
"""

import argparse
import csv  # import standard "csv" module
import logging


def parse_args():
    """Parse arguments and set up logging verbosity.

    :rtype: parsed arguments as Namespace object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename",
                        help="setting file", metavar="FILE")
    parser.add_argument("-e", "--encoding", dest="encoding", default='utf8',
                        help="input file encoding")
    parser.add_argument("-o", "--output", dest="output",
                        help="output file", metavar="FILE")
    parser.add_argument("-n", "--dryrun", dest="dryrun",
                        help="dry run", default=False, action="store_true")
    parser.add_argument("-v", "--verbose", dest="verbose", default=False,
                        action="store_true", help="verbose mode")
    parser.add_argument("-q", "--quiet", dest="quiet", default=False,
                        action="store_true", help="quiet mode")
    parser.add_argument("filename", nargs=1, help="CSV file path")

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    elif not args.quiet:
        logging.basicConfig(level=logging.INFO)

    return args


def process(args):
    """Parse daily Tokyo stock prices, and calculate up/down.
    """
    with open(args.filename[0], encoding=args.encoding) as fp:
        reader = csv.reader(fp)  # Instantiate CSV reader with file pointer.
        header = next(reader)
        for t in reader:
            dt = dict(zip(header, t))  # Bind header and row
            day = dt['データ日付']
            # Calculate the differenciate of the day.
            diff = float(dt['終値']) - float(dt['始値'])
            if diff > 0:
                message = 'up'
            elif diff < 0:
                message = 'down'
            else:
                message = 'same'
            # Write out day, up/down/same, and diff.
            print(f'{day}\t{message:5}\t{round(diff, 2)}')


def main():
    args = parse_args()
    process(args)


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
