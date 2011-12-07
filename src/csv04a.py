#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""%prog [options] csv_file
"""

import os

from pyschool.unicodecsv import UnicodeReader
from pyschool.cmdline import parse_args

DEFAULT_CSV_FILE = 'sample.csv'


class LeagueStats(object):

    def __init__(self, rank, team, point, match, goaldiff):
        self.rank = int(rank)
        self.team = team
        self.point = int(point)
        self.match = int(match)
        self.goaldiff = int(goaldiff)

    def to_str(self, delim='\t'):
        return "%d\t%s\t%d\t%d\t%d" % (self.rank, self.team,
                    self.point, self.match, self.goaldiff)


def csv2tsv(fname):
    """Convert a CSV format file to TSV format string.
    """
    with open(fname) as reader:
        for row in UnicodeReader(reader):
            record = LeagueStats(*row)
            print record.to_str()


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
