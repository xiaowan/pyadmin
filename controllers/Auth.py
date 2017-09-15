#!/usr/bin/env python

from library.Handlers import BaseHandler
from service.AuthService import AuthService


class AuthListHandler(BaseHandler):
    def get(self, *args, **kwargs):
        res = AuthService().get_auths()
        self.json(res)


class AddAuthHandler(BaseHandler):
    def post(self, *args, **kwargs):
        name = self.post_arguments.get('name', None)
        code = self.post_arguments.get('code', None)
        res = AuthService().add_auth(name, code)
        self.json(res)


route = [
    (r'/auth/list', AuthListHandler), # 所有权限列表
    (r'/auth/add', AddAuthHandler), # 新增权限
]

