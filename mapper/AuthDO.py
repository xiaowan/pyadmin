#!/usr/bin/env python

from .BaseDO import BaseDO
from sqlalchemy import Column
from sqlalchemy.types import *


class AuthDO(BaseDO):
    __tablename__='py_auth'

    name = Column(String, nullable=False)
    code = Column(String, nullable=False)