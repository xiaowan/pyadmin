#!/usr/bin/env python


from library.Result import Result
from library.Decorate import Transaction
from .BaseService import BaseService
from dao.AuthDAO import AuthDAO

from mapper.AuthDO import AuthDO


class AuthService(BaseService):
    """ 角色相关类 """
    def __init__(self):
        self.authDAO = AuthDAO.getInstance()
        super().__init__()

    def get_auths(self):
        """ 获取所有的权限 """
        auths = self.authDAO.get_auth()
        return Result(code=0, data=auths)

    @Transaction(name="session")
    def add_auth(self, name=None, code=None):
        """ 新增权限 """
        obj = AuthDO()
        obj.name = name
        obj.code = code
        self.authDAO.add_auth(obj)
        return Result(code=0)
