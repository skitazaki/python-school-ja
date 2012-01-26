#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Download weather forecast around Tokyo.
"""

import logging
import urllib
import urllib2
from xml.dom.minidom import parse

API = "http://www.google.com/ig/api?weather=Tokyo"


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


def main():
    r = request(API)
    xml = parse(r)
    for n in xml.getElementsByTagName("forecast_conditions"):

        def data(name):
            elems = n.getElementsByTagName(name)
            if elems:
                return ", ".join(map(lambda e: e.getAttribute("data"), elems))
            else:
                logging.error("%s tag was not found.", name)

        print "%5s\t%-20s\t%3s\t%3s" % (data("day_of_week"), data("condition"),
                                    data("low"), data("high"))

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
