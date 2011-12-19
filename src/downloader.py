#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""%prog url [, url [, ... ]]

Download contents from given URL list.
"""

import logging
import os
import urllib
from urlparse import urlparse

# Check the document about version differences.
# http://docs.python.org/library/urlparse.html#urlparse.parse_qs
#     New in version 2.6: Copied from the cgi module.
try:
    from urlparse import parse_qs
except ImportError:
    from cgi import parse_qs

from pyschool.cmdline import parse_args


def download(url):
    o = urlparse(url)
    # Check the document for return value attributes.
    # http://docs.python.org/library/urlparse.html#urlparse.urlparse
    # "index 2" means "path" attribute, Hierarchical path.
    path = o[2]
    fname = os.path.basename(path)
    if os.path.exists(fname):
        logging.warn("%s already exists, overwrite it.", fname)
    logging.info("Download: %s -> %s", url, fname)
    try:
        r = urllib.urlretrieve(url, fname)
    except IOError, e:
        logging.error(e)


def main():
    opts, args = parse_args()
    if not args:
        # Dirty code. This replacement should be in `parse_args()`.
        raise SystemExit(__doc__.replace("%prog", os.path.basename(__file__)))
    for url in args:
        download(url)

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
