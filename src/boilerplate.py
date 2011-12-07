#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""%prog [options] args
"""

import logging
import os
import optparse


def parse_args():
    """Parse arguments and sets up logging verbosity.

    :rtype: normal options and arguments as tuple.
    """
    parser = optparse.OptionParser(__doc__)
    parser.add_option("-f", "--file", dest="filename",
        help="setting file", metavar="FILE")
    parser.add_option("-o", "--output", dest="output",
        help="output file", metavar="FILE")
    parser.add_option("-n", "--dryrun", dest="dryrun",
        help="dry run", default=False, action="store_true")
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


def proc():
    """Main procedure with some tests.
    """
    pass

def main():
    opts, args = parse_args()


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
