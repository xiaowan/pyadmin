#!/usr/bin/env python

from .BaseService import BaseService
from dao.AuthDAO import AuthDAO
from dao.RoleDAO import RoleDAO
from library.Decorate import Transaction
from mapper.AuthDO import AuthDO
from library.Route import route
from library.Exception import AuthException


class AuthService(BaseService):

    def __init__(self):
        self.authDAO = AuthDAO.getInstance()
        self.roleDAO = RoleDAO.getInstance()
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
        exists_auth = self.authDAO.get_auths()
        exists_auth_list = [auth.code for auth in exists_auth]

        url_mappers = route.get_urls()
        auths = [url_mapper[0] for url_mapper in url_mappers if url_mapper[0] not in exists_auth_list]

        return auths

    def get_assign_for_role(self):
        """ 所有可以分配给角色的权限 """
        # 所有已经分配的权限点
        assigned_auths_obj = self.roleDAO.get_auths_by_role(role=None)
        assigned_auth_ids = [ assigned_auth.auth_id for assigned_auth in assigned_auths_obj ]

        def _filter(x):
            if x.id not in assigned_auth_ids:
                return x

        return list(filter(_filter, self.authDAO.get_auths()))
