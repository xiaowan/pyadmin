#!/usr/bin/env python

from .BaseDO import BaseDO
from sqlalchemy import Column
from sqlalchemy.types import *


class UmUserDO(BaseDO):
    __tablename__ = 'um_user'

    loginname = Column(String, nullable=True)
    nickname = Column(String, nullable=True)
    password = Column(String, nullable=True)
    is_valid = Column(VARCHAR, nullable=False, default='yes')
    is_relation = Column(String, nullable=False, default='no')
    avatar = Column(String, nullable=False, default="/static/img/avatar.png")
    token = Column(String, nullable=True)
    access_token = Column(TEXT, nullable=True)
