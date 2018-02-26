#!/usr/bin/env python

from .BaseDO import BaseDO
from sqlalchemy import Column
from sqlalchemy.types import *


class UmPowerDO(BaseDO):
    __tablename__ = 'py_power'

    power = Column(String, nullable=False)
    name = Column(String, nullable=False)
    desc = Column(Text, nullable=False)
