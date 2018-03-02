#!/usr/bin/env python

from .BaseService import BaseService
from dao.RoleDAO import RoleDAO
from dao.AuthDAO import AuthDAO
from library.Exception import RoleException
from mapper.RoleDO import RoleDO
from mapper.RoleAuthsDO import RoleAuthsDO
from library.Decorate import Transaction


class RoleService(BaseService):

    def __init__(self):
        self.roleDAO = RoleDAO.getInstance()
        self.authDAO = AuthDAO.getInstance()
        super().__init__()

    def get_roles(self):
        """ 获取所有角色 """
        return self.roleDAO.get_roles()

    @Transaction(name="session")
    def add_role(self, name=None, role=None, desc=None):
        """ 新增角色 """
        exist_role = self.roleDAO.get_role_by_role(role=role)

        if exist_role:
            raise RoleException(13000)

        role_obj = RoleDO()
        role_obj.name = name
        role_obj.role = role
        role_obj.desc = desc

        self.roleDAO.add_role(role_obj)
        return True

    def get_auths_by_role(self, role=None):
        """ 指定角色下的所有权限点 """
        role_auth_objs = self.roleDAO.get_auths_by_role(role=role)

        auth_objs = self.authDAO.get_auths()
        auths = {auth.id: auth.name for auth in auth_objs}

        def make_group(auth):
            return {
                'auth_id': auth.auth_id,
                'name': auths[auth.auth_id]
            }

        return list(map(make_group, role_auth_objs))

    @Transaction(name="session")
    def add_auths_for_role(self, role=None, auths=[]):
        """ 为指定角色新增权限点 """

        def make_obj(x):
            tmp = RoleAuthsDO()
            tmp.role = role
            tmp.auth_id = x
            return tmp

        self.roleDAO.save(list(map(make_obj, auths)))

    @Transaction(name="session")
    def del_auths_for_role(self, role=None, auths=[]):
        """ 为指定角色删除权限点 """
        return self.roleDAO.remove_auths_for_role(role=role, auths=auths)
