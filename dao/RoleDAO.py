#!/usr/bin/env python


from sqlalchemy import desc
from .BaseDAO import BaseDAO
from mapper.RoleDO import RoleDO
from mapper.RoleAuthsDO import RoleAuthsDO


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

    def get_auths_by_role(self, role=None):
        """ 指定role下的所有权限点 """
        query = self.session.query(RoleAuthsDO)
        if role is not None:
            query = query.filter(RoleAuthsDO.role == role)

        return query.all()

    def remove_auths_for_role(self, role, auths=[]):
        return self.session.query(RoleAuthsDO).filter(RoleAuthsDO.auth_id.in_(auths)).filter(RoleAuthsDO.role == role).delete(synchronize_session=False)

