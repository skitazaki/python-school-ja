#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""%prog [options] csv_file
"""

from csv import DictReader
import os

from pyschool.cmdline import parse_args

DEFAULT_CSV_FILE = 'sample.csv'


def csv2tsv(fname):
    """Convert a CSV format file to TSV format string.
    """
    with open(fname) as reader:
        stream = DictReader(reader)
        for record in stream:
            # XXX: Convert encodings.
            print record['rank'] + '\t' + \
                  record['team'] + '\t' + \
                  record['point'] + '\t' + \
                  record['match'] + '\t' + \
                  record['goaldiff']


def main():
    opts, args = parse_args(__doc__)
    fname = args[0] if args else DEFAULT_CSV_FILE
    if not os.path.exists(fname):
        raise SystemExit("\"%s\" is not found." % (fname,))
    csv2tsv(fname)


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
