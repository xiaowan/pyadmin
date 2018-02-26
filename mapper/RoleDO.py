#!/usr/bin/env python

from .BaseDO import BaseDO
from sqlalchemy import Column
from sqlalchemy.types import *


class UmRoleDO(BaseDO):
    __tablename__ = 'py_role'

    role = Column(String, nullable=False)
    alias = Column(String, nullable=False)
    desc = Column(Text, nullable=False)
