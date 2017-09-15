#!/usr/bin/env python

from .BaseDAO import BaseDAO
from mapper.UserRolesDO import UserRolesDO
from mapper.RoleDO import RoleDO
from mapper.RoleAuthsDO import RoleAuthsDO


class RoleDAO(BaseDAO):
    """ 角色类相关原子操作 """
    def get_user_roles(self, uid=None):
        """ 获取用户所有角色 """
        return self.session.query(UserRolesDO).filter(UserRolesDO.uid == uid).all()

    def get_all_role(self):
        """ 获取所有角色 """
        return self.session.query(RoleDO).all()

    def add_role(self, role):
        """ 增加角色 """
        self.session.add(role)
        self.session.flush()

    def get_auths_by_role(self, role):
        """ 获取指定角色下的所有权限 """
        return self.session.query(RoleAuthsDO).filter(RoleAuthsDO.role == role).all()

    def add_auths(self, objs=[]):
        """ 新增权限 """
        self.session.add_all(objs)
        self.session.flush()

    def del_auths(self, role, auths=[]):
        """ 删除权限 """
        self.session.query(RoleAuthsDO).filter(RoleAuthsDO.role == role).\
            filter(RoleAuthsDO.auth_id.in_(auths)).delete(synchronize_session=False)