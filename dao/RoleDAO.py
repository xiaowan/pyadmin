#!/usr/bin/env python


from sqlalchemy import desc
from .BaseDAO import BaseDAO
from mapper.RoleDO import RoleDO


class RoleDAO(BaseDAO):
    def get_roles(self):
        """ 获取所有角色 """
        return self.session.query(RoleDO).order_by(desc(RoleDO.id)).all()

    def get_role_by_role(self, role=None):
        return self.session.query(RoleDO).filter(RoleDO.role == role).first()

    def add_role(self, obj):
        """ 添加角色 """
        self.session.add(obj)
        self.session.flush()
