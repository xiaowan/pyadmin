#!/usr/bin/env python

from . BaseService import BaseService
from dao.AuthDAO import AuthDAO
from library.Decorate import Transaction
from mapper.AuthDO import AuthDO

class AuthService(BaseService):

    def __init__(self):
        self.authDAO = AuthDAO.getInstance()
        super().__init__()

    def get_all_auths(self):
        return self.authDAO.get_auths()

    @Transaction(name="session")
    def add_auth(self, name=None, auth_code=None):
        """ 添加auth """
        auth_obj = AuthDO()
        auth_obj.name = name
        auth_obj.code = auth_code

        return self.authDAO.add_auth(auth_obj)


