#!/usr/bin/env python

from library.Handlers import BaseHandler
from service.RoleService import RoleService


class RoleListHandler(BaseHandler):
    def get(self, *args, **kwargs):
        res = RoleService().get_roles()
        self.json(res)


class AddRoleHandler(BaseHandler):
    def post(self, *args, **kwargs):
        name = self.post_arguments.get('name', None)
        code = self.post_arguments.get('code', None)
        res = RoleService().add_role(name, code)
        self.json(res)


class GetAuthByRoleHandler(BaseHandler):
    def get(self, *args, **kwargs):
        role = self.get_argument('role', None)
        res = RoleService().get_auths(role)
        self.json(res)


class RoleAddAuthHandler(BaseHandler):
    def post(self, *args, **kwargs):
        role = self.post_arguments.get('role', None)
        auths = self.post_arguments.get('auths', None)
        res = RoleService().add_auth_for_role(role, auths)
        self.json(res)


class RoleDelAuthHandler(BaseHandler):
    def post(self, *args, **kwargs):
        role = self.post_arguments.get('role', None)
        auths = self.post_arguments.get('auths', None)
        res = RoleService().del_auth_for_role(role, auths)
        self.json(res)


route = [
    (r'/role/list', RoleListHandler), # 所有角色列表
    (r'/role/add', AddRoleHandler), # 新增角色
    (r'/role/auths', GetAuthByRoleHandler), # 指定角色的所有权限
    (r'/role/auth/add', RoleAddAuthHandler), # 指定角色新增权限
    (r'/role/auth/del', RoleDelAuthHandler), # 指定角色删除权限
]

