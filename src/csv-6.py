#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Parse daily Tokyo stock prices.
"""

import csv
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Date

from pyschool.cmdline import parse_args

# SQLite On-Memory storage for test run.
DEFAULT_SQLITE_FILE = ':memory:'

# Declare input fields definition.
FIELDS = (
    {'id': 'day', 'type': 'datetime', 'format': '%Y-%m-%d'},
    {'id': 'price_begin', 'type': 'float'},
    {'id': 'price_max', 'type': 'float'},
    {'id': 'price_min', 'type': 'float'},
    {'id': 'price_end', 'type': 'float'}
)

Session = sessionmaker()
Base = declarative_base()


class StockPrice(Base):

    __tablename__ = 'stock_price'

    id = Column(Integer, primary_key=True)
    day = Column(Date, nullable=False, unique=True)
    price_begin = Column(Float, nullable=False)
    price_max = Column(Float, nullable=False)
    price_min = Column(Float, nullable=False)
    price_end = Column(Float, nullable=False)

    def __repr__(self):
        return "<StockPrice('{}')>".format(self.day)

    def diff(self):
        return self.price_end - self.price_begin


def process(args):
    """Parse daily Tokyo stock prices, and calculate up/down.
    After that, import them into SQLite database.
    """
    # Prepare database connection, table, and session.
    dsl = 'sqlite:///' + (args.output or DEFAULT_SQLITE_FILE)
    engine = create_engine(dsl, echo=True)
    Base.metadata.create_all(engine)
    Session.configure(bind=engine)
    session = Session()
    with open(args.filename[0]) as fp:
        reader = csv.reader(fp)  # Instantiate CSV reader with file pointer.
        for t in reader:
            # Convert input values to declared name and type.
            dt = {}
            for i, f in enumerate(FIELDS):
                if f['type'] == 'integer':
                    dt[f['id']] = int(t[i])
                elif f['type'] == 'float':
                    dt[f['id']] = float(t[i])
                elif f['type'] == 'datetime':
                    dt[f['id']] = datetime.datetime.strptime(t[i], f['format'])
                else:
                    dt[f['id']] = t[i]
            # Instantiate SQLAlchemy data model object.
            p = StockPrice(**dt)
            # Show the same things with previous scripts.
            diff = p.diff()
            if diff > 0:
                message = 'up'
            elif diff < 0:
                message = 'down'
            else:
                message = 'same'
            # Write out day, up/down/same, and diff.
            print('{}\t{:5}\t{}'.format(p.day, message, round(diff, 2)))
            session.add(p)
    # Don't forget to commit the changes you add.
    session.commit()


def main():
    args = parse_args()
    process(args)


def test():
    pass

if __name__ == '__main__':
    main()

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :
