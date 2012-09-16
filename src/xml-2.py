#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Usage: %prog [options] {POM_FILE}
"""

import logging
import os
from xml.etree.ElementTree import parse

from pyschool.cmdline import parse_args


class InvalidArtifact(Exception):
    pass


class Artifact(object):

    NAMESPACE = "http://maven.apache.org/POM/4.0.0"
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
        element = xml.find('{%s}artifactId' % (Artifact.NAMESPACE,))
        if element is None:
            raise InvalidArtifact("'artifactId' is missing in " + pom)
        artifact = Artifact(element.text)
        element = xml.find('{%s}groupId' % (Artifact.NAMESPACE,))
        if element is None:
            logging.info("'groupId' is missing in " + pom)
        else:
            artifact.groupId = element.text
        element = xml.find('{%s}version' % (Artifact.NAMESPACE,))
        if element is None:
            logging.info("'groupId' is missing in " + pom)
        else:
            artifact.version = element.text
        return artifact


def main():
    opts, args = parse_args()

    if len(args) != 1:
        raise SystemExit(__doc__)
    pom = args[0]
    if not os.path.exists(pom):
        raise SystemExit(pom + ' was not found.')

    artifact = Artifact.from_pom_file(pom)
    print artifact


def test():
    fname = "etc/xml-1.xml"
    artifact = Artifact.from_pom_file(fname)
    print artifact

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
