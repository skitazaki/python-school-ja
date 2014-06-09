#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parse Maven POM file.
"""

import logging
import os
from xml.dom.minidom import parse

from pyschool.cmdline import parse_args


class InvalidArtifact(Exception):
    pass


class Artifact(object):

    DEFAULT_GROUP = 'sample-group'
    DEFAULT_VERSION = '1.0.0-SNAPSHOT'

    def __init__(self, artifactId, groupId=None, version=None):
        self.artifactId = artifactId
        self.groupId = groupId or Artifact.DEFAULT_GROUP
        self.version = version or Artifact.DEFAULT_VERSION

    def __repr__(self):
        return "%s/%s/%s" % (self.groupId, self.artifactId, self.version)

    @staticmethod
    def from_pom_file(pom):
        xml = parse(pom)
        els = xml.getElementsByTagName('artifactId')
        if els:
            artifact = Artifact(els[0].firstChild.data)
        else:
            raise InvalidArtifact("'artifactId' is missing in " + pom)
        els = xml.getElementsByTagName('groupId')
        if els:
            artifact.groupId = els[0].firstChild.data
        else:
            logging.info("'groupId' is missing in " + pom)
        els = xml.getElementsByTagName('version')
        if els:
            artifact.version = els[0].firstChild.data
        else:
            logging.info("'groupId' is missing in " + pom)
        return artifact


def main():
    args = parse_args()
    fname = args.filename[0]
    if not os.path.exists(fname):
        raise SystemExit('"{}" is not found.'.format(fname))
    artifact = Artifact.from_pom_file(fname)
    print(artifact)


def test():
    fname = "etc/xml-1.xml"
    artifact = Artifact.from_pom_file(fname)
    assert 'sample-group/sample-group-commons/1.0.0' == repr(artifact)

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
