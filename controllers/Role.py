#!/usr/bin/env python

from library.Handlers import BaseHandler
from library.Decorate import Return
from library.Route import route
from library.Exception import UserException
from service.RoleService import RoleService


@route(r'/role/list')
class RoleListHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        return RoleService().get_roles()


@route(r'/role/add')
class AddRoleHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        name = self.post_arguments.get('name', None)
        role = self.post_arguments.get('role', None)
        desc = self.post_arguments.get('desc', None)
        if role is None:
            raise UserException(code=10001, desc="请填写角色代号")
        if name is None:
            raise UserException(code=10001, desc="请填写角色名称")

        return RoleService().add_role(name=name, role=role, desc=desc)


@route(r'/role/auths')
class RoleAuthsHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        """ 指定角色下的所有权限点 """
        role = self.get_argument('role', default=None)
        return RoleService().get_auths_by_role(role=role)


@route(r'/role/auth/add')
class RoleAuthAddHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        role = self.post_arguments.get('role', None)
        auth_ids = self.post_arguments.get('auths', None)
        return RoleService().add_auths_for_role(role=role, auths=auth_ids)


@route(r'/role/auth/del')
class RoleAuthDelHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        role = self.post_arguments.get('role', None)
        auth_ids = self.post_arguments.get('auths', None)
        return RoleService().del_auths_for_role(role=role, auths=auth_ids)
