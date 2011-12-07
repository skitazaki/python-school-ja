# -*- coding: utf-8 -*-

"""Simple Command Line Utility.
"""

import logging
import optparse


def parse_args(doc=None):
    """Parse arguments and sets up logging verbosity.

    :rtype: normal options and arguments as tuple.
    """
    parser = optparse.OptionParser(doc)
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

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
