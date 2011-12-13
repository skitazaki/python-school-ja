#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""%prog [options] csv_file [sqlite_file]
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from pyschool.unicodecsv import UnicodeReader
from pyschool.cmdline import parse_args

DEFAULT_CSV_FILE = 'sample.csv'
DEFAULT_SQLITE_FILE = ':memory:'

Session = sessionmaker()
Base = declarative_base()


class LeagueStats(Base):

    __tablename__ = 'league_stats'

    id = Column(Integer, primary_key=True)
    team = Column(String)
    rank = Column(Integer)
    point = Column(Integer)
    match = Column(Integer)
    goaldiff = Column(Integer)

    def __repr__(self):
        return "<LeagueStats('%s:%d')>" % (self.team, self.point)


def csv2sqlite(fname, output):
    """Import a CSV format file to SQLite database.
    """
    dsl = 'sqlite:///' + output
    engine = create_engine(dsl, echo=True)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()
    with open(fname) as reader:
        stream = UnicodeReader(reader)
        # Read a header line.
        fields = stream.next()
        for row in stream:
            record = dict(zip(fields, row))
            r = LeagueStats(team=record['team'],
                    rank=int(record['rank']),
                    point=int(record['point']),
                    match=int(record['match']),
                    goaldiff=int(record['goaldiff']))
            session.add(r)
    session.commit()


def main():
    opts, args = parse_args(__doc__)
    fname = args[0] if args else DEFAULT_CSV_FILE
    if not os.path.exists(fname):
        raise SystemExit("\"%s\" is not found." % (fname,))
    out = args[1] if len(args) > 1 else DEFAULT_SQLITE_FILE
    csv2sqlite(fname, out)


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
