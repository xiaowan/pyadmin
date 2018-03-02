#!/usr/bin/env python


from sqlalchemy import desc
from .BaseDAO import BaseDAO
from library.Decorate import Transaction
from mapper.RoleDO import RoleDO


class RoleDAO(BaseDAO):
    def get_roles(self):
        """ 获取所有角色 """
        return self.session.query(RoleDO).order_by(desc(RoleDO.id)).all()

    @Transaction(name="session")
    def add_role(self, role=None, alias=None, desc=None):
        """ 添加角色 """
        obj = RoleDO()
        obj.role = role
        obj.alias = alias
        obj.desc = desc
        self.session.add(obj)
        return obj
