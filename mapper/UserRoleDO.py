#!/usr/bin/env python

from .BaseDO import BaseDO
from sqlalchemy import Column
from sqlalchemy.types import *


class UserRoleDO(BaseDO):
    __tablename__ = 'um_user_role'

    uid = Column(Integer, nullable=False)
    role = Column(String, nullable=False)
