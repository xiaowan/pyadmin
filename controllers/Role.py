#!/usr/bin/env python

from library.Handlers import BaseHandler
from library.Decorate import Return
from library.Route import route
from library.Exception import UserException
from dao.RoleDAO import RoleDAO


@route(r'/role/list')
class RoleListHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        return RoleDAO().get_roles()


@route(r'/role/add')
class AddRoleHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        role = self.post_arguments.get('role', None)
        alias = self.post_arguments.get('alias', None)
        desc = self.post_arguments.get('desc', None)
        if role is None:
            raise UserException(code=10001, desc="请填写角色")
        if alias is None:
            raise UserException(code=10001, desc="请填写角色别名")
        if desc is None:
            raise UserException(code=10001, desc="请填写角色职能")

        return RoleDAO().add_role(role, alias, desc)
