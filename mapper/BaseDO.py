#!/usr/bin/env python

import time
from uuid import uuid4
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base


class Base(object):
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    id = Column(Integer, primary_key=True, default=lambda: str(uuid4()))
    create_time = Column(Integer, default=lambda: int(time.time()))

    @property
    def dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.dict)

BaseDO = declarative_base(cls=Base)


