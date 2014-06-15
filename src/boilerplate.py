#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""%prog [options] args
"""

import argparse
import logging


def parse_args():
    """Parse arguments and set up logging verbosity.

    :rtype: parsed arguments as Namespace object.
    """
    parser = argparse.ArgumentParser(__doc__)
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

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    elif not args.quiet:
        logging.basicConfig(level=logging.INFO)

    return args


def process(args):
    """Main procedure with some tests.
    """
    pass


def main():
    args = parse_args()
    process(args)


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
