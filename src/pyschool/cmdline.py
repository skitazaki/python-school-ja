# -*- coding: utf-8 -*-

"""Simple Command Line Utility.
"""

import argparse
import logging


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
                        help="encoding of input file")
    parser.add_argument("-o", "--output", dest="output", metavar="FILE",
                        help="output file path")
    parser.add_argument("filename", nargs=1, help="input file path")

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    elif not args.quiet:
        logging.basicConfig(level=logging.INFO)

    return args

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
