#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""%prog [options] {search-word-for-twitter}
"""

import json
import logging
import sys
import urllib
import urllib2

from pyschool.cmdline import parse_args

TWITTER_SEARCH_API = "http://search.twitter.com/search.json"


def request(url, params=None):
    logging.debug("Request URL: %s", url)
    if params:
        if url.find('?') < 0:
            url += '?'
        url += urllib.urlencode(params)
    try:
        r = urllib2.urlopen(url)
        headers = []
        info = r.info()
        for k in info:
            headers.append(k + "=" + info[k])
        logging.debug("Response Header: %s" % ",".join(headers))
        return r
    except urllib2.HTTPError, e:
        logging.error(e)
    except urllib2.URLError, e:
        logging.error(e)


def twitter_search(word):
    """Use Twitter API Sample.
    """
    logging.info("Input word: %s", word)
    params = dict(q=word.encode("utf-8"))
    result = request(TWITTER_SEARCH_API, params)
    r = json.load(result)
    for t in r["results"]:
        txts = t["text"].split()
        if len(txts) > 5:
            txts = txts[:5] + ["...",]
        try:
            print "[%-20s] %s" % (t["from_user_name"], " ".join(txts))
        except:
            pass


def main():
    opts, args = parse_args(__doc__)
    if len(args) != 1:
        raise SystemExit(__doc__)
    word = args[0].decode(sys.stdin.encoding)
    twitter_search(word)


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
