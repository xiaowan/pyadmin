#!/usr/bin/env python

from .BaseDO import BaseDO
from sqlalchemy import Column
from sqlalchemy.types import *


class UserDO(BaseDO):
    __tablename__='py_user'

    nickname = Column(String, nullable=False)
    loginname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_valid = Column(String, nullable=False)
    token = Column(String, nullable=True)
    avatar = Column(String, nullable=False, default='/static/img/avatar.png')
