#!/usr/bin/env python

from .BaseDO import BaseDO
from sqlalchemy import Column
from sqlalchemy.types import *


class RoleAuthsDO(BaseDO):
    __tablename__='py_role_auths'

    role = Column(String, nullable=False)
    auth_id = Column(String, nullable=False)