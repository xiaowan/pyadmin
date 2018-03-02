#!/usr/bin/env python

from .BaseDO import BaseDO
from sqlalchemy import Column
from sqlalchemy.types import *


class UserDO(BaseDO):
    __tablename__ = 'py_user'

    loginname = Column(String, nullable=True)
    nickname = Column(String, nullable=True)
    password = Column(String, nullable=True)
    is_valid = Column(VARCHAR, nullable=False, default='yes')
    avatar = Column(String, nullable=False, default="/static/img/avatar.png")
    token = Column(String, nullable=True)
