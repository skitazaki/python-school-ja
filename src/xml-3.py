#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parse Maven POM file.
"""

import os
import logging
import xml.sax
from xml.sax.handler import ContentHandler

from pyschool.cmdline import parse_args


class Artifact(object):

    DEFAULT_GROUP = 'sample-group'
    DEFAULT_VERSION = '1.0.0-SNAPSHOT'

    def __init__(self, artifactId, groupId=None, version=None):
        self.artifactId = artifactId
        self.groupId = groupId or Artifact.DEFAULT_GROUP
        self.version = version or Artifact.DEFAULT_VERSION

    def __repr__(self):
        return "%s/%s/%s" % (self.groupId, self.artifactId, self.version)


class ArtifactParser(ContentHandler):

    targets = (
                "artifactId",
                "groupId",
                "version"
              )
    artifact = {}
    _current = None

    def startElement(self, name, attrs):
        if name in self.targets:
            self._current = name
            self.artifact[self._current] = ''

    def endElement(self, name):
        pass

    def characters(self, content):
        c = content.strip()
        if self._current and c:
            self.artifact[self._current] += c


def main():
    args = parse_args()
    fname = args.filename[0]
    if not os.path.exists(fname):
        raise SystemExit('"{}" is not found.'.format(fname))
    parser = ArtifactParser()
    xml.sax.parse(fname, parser)
    print(Artifact(**(parser.artifact)))


def test():
    fname = "etc/xml-1.xml"
    parser = ArtifactParser()
    xml.sax.parse(fname, parser)
    artifact = Artifact(**(parser.artifact))
    assert 'sample-group/sample-group-commons/1.0.0' == repr(artifact)

if __name__ == "__main__":
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
