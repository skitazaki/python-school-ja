#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parse daily Tokyo stock prices.
"""

import argparse
import csv  # import standard "csv" module
import logging

# Declare fields definition.
FIELDS = (
    {'id': 'day', 'type': 'string'},
    {'id': 'price_begin', 'type': 'float'},
    {'id': 'price_max', 'type': 'float'},
    {'id': 'price_min', 'type': 'float'},
    {'id': 'price_end', 'type': 'float'}
)


def parse_args():
    """Parse arguments and set up logging verbosity.

    :rtype: parsed arguments as Namespace object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename",
                        help="setting file", metavar="FILE")
    parser.add_argument("-o", "--output", dest="output",
                        help="output file", metavar="FILE")
    parser.add_argument("-n", "--dryrun", dest="dryrun",
                        help="dry run", default=False, action="store_true")
    parser.add_argument("-v", "--verbose", dest="verbose", default=False,
                        action="store_true", help="verbose mode")
    parser.add_argument("-q", "--quiet", dest="quiet", default=False,
                        action="store_true", help="quiet mode")
    # Add this line from boilerplate.
    parser.add_argument("--header", dest="header", default=False,
                        action="store_true", help="contains header row")
    parser.add_argument("--encoding", dest="encoding", default='utf-8',
                        help="Encoding of input file")
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
    header = tuple(map(lambda f: f['id'], FIELDS))
    with open(args.filename[0], encoding=args.encoding) as fp:
        reader = csv.reader(fp)  # Instantiate CSV reader with file pointer.
        if args.header:
            _ = next(reader)
            logging.info('Skip header row: %s', _)
        else:
            logging.info('No header row is to be in input file.')
        for t in reader:
            dt = dict(zip(header, t))  # Bind header and row
            # Calculate the differenciate of the day.
            diff = float(dt['price_end']) - float(dt['price_begin'])
            if diff > 0:
                message = 'up'
            elif diff < 0:
                message = 'down'
            else:
                message = 'same'
            # Write out day, up/down/same, and diff.
            print('{}\t{:5}\t{}'.format(dt['day'], message, round(diff, 2)))


def main():
    args = parse_args()
    process(args)


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
