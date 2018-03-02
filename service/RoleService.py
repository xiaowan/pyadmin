#!/usr/bin/env python

from . BaseService import BaseService
from dao.RoleDAO import RoleDAO
from library.Exception import RoleException
from mapper.RoleDO import RoleDO
from library.Decorate import Transaction


class RoleService(BaseService):

    def __init__(self):
        self.roleDAO = RoleDAO.getInstance()
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