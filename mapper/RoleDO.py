#!/usr/bin/env python

from .BaseDO import BaseDO
from sqlalchemy import Column
from sqlalchemy.types import *


class RoleDO(BaseDO):
    __tablename__ = 'py_role'

    role = Column(String, nullable=False)
    name = Column(String, nullable=False)
    desc = Column(Text, nullable=False)
