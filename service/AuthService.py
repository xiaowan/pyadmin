#!/usr/bin/env python

from . BaseService import BaseService
from dao.AuthDAO import AuthDAO
from library.Decorate import Transaction
from mapper.AuthDO import AuthDO
from library.Route import route
from library.Exception import AuthException

class AuthService(BaseService):

    def __init__(self):
        self.authDAO = AuthDAO.getInstance()
        super().__init__()

    def get_all_auths(self):
        return self.authDAO.get_auths()

    @Transaction(name="session")
    def add_auth(self, name=None, auth_code=None):
        """ 添加auth """

        exist_auth = self.authDAO.get_auth_by_code(code=auth_code)

        if exist_auth is not None:
            raise AuthException(12000)

        auth_obj = AuthDO()
        auth_obj.name = name
        auth_obj.code = auth_code

        return self.authDAO.add_auth(auth_obj)


    def get_new_auths(self):
        """ 获取所有未被添加的权限 """
        auths = []
        urls = route.get_urls()
        for auth in urls:
            auths.append(auth[0])
        return auths