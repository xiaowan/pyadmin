#!/usr/bin/env python


from library.Result import Result
from library.Decorate import Transaction
from .BaseService import BaseService
from dao.RoleDAO import RoleDAO

from mapper.RoleDO import RoleDO
from mapper.RoleAuthsDO import RoleAuthsDO

class RoleService(BaseService):
    """ 角色相关类 """
    def __init__(self):
        self.roleDAO = RoleDAO.getInstance()
        super().__init__()

    def get_roles(self):
        """ 获取所有role """
        res = self.roleDAO.get_all_role()
        return Result(code=0 , data=res)

    @Transaction(name="session")
    def add_role(self, name=None, code=None):
        """ 新增角色 """
        obj = RoleDO()
        obj.name = name
        obj.code = code
        self.roleDAO.add_role(obj)
        return Result(code=0)

    def get_auths(self, role):
        """ 获取指定角色下的所有权限 """
        res = self.roleDAO.get_auths_by_role(role)
        return Result(code=0 ,data=res)

    @Transaction(name="session")
    def add_auth_for_role(self, role, auths=[]):
        """ 指定role新增权限 """
        if auths:
            objs = []
            for x in auths:
                tmp = RoleAuthsDO()
                tmp.role = role
                tmp.auth_id = x
                objs.append(tmp)
                del tmp
            self.roleDAO.add_auths(objs)

        return Result(code=0)

    @Transaction(name="session")
    def del_auth_for_role(self, role, auths=[]):
        """ 指定role删除权限 """
        self.roleDAO.del_auths(role, auths)
        return Result(code=0)