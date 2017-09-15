#!/usr/bin/env python

from .BaseDO import BaseDO
from sqlalchemy import Column
from sqlalchemy.types import *


class UserRolesDO(BaseDO):
    __tablename__='py_user_roles'

    uid = Column(String, nullable=False)
    role = Column(String, nullable=False)
