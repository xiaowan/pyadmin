#!/usr/bin/env python

import time
from uuid import uuid4
from sqlalchemy import String, Integer
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base


class Base(object):
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    @property
    def columnitems(self):
        return dict([(c, getattr(self, c)) for c in self.columns])

    @property
    def dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.columnitems)

    def tojson(self):
        return self.columnitems


class BaseObj(Base):
    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    create_time = Column(Integer, default=lambda: int(time.time()))


BaseDO = declarative_base(cls=BaseObj)
