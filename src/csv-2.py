#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""%prog [options] csv_file
"""

import csv
import logging
import optparse
import os

DEFAULT_CSV_FILE = 'sample.csv'


def parse_args():
    """Parse arguments and sets up logging verbosity.

    :rtype: normal options and arguments as tuple.
    """
    parser = optparse.OptionParser(__doc__)
    parser.add_option("-o", "--output", dest="output",
        help="output file", metavar="FILE")
    parser.add_option("-v", "--verbose", dest="verbose",
        default=False, action="store_true", help="verbose mode")
    parser.add_option("-q", "--quiet", dest="quiet",
        default=False, action="store_true", help="quiet mode")

    opts, args = parser.parse_args()

    if opts.verbose:
        logging.basicConfig(level=logging.DEBUG)
    elif not opts.quiet:
        logging.basicConfig(level=logging.INFO)

    return opts, args


def csv2tsv(fname):
    """Convert a CSV format file to TSV format string.
    """
    with open(fname) as reader:
        for row in csv.reader(reader):
            print '\t'.join(row)


def main():
    opts, args = parse_args()
    fname = args[0] if args else DEFAULT_CSV_FILE
    if not os.path.exists(fname):
        raise SystemExit(fname + " is not found.")
    csv2tsv(fname)


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
