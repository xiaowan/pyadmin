#!/usr/bin/env python

from library.Handlers import BaseHandler
from library.Decorate import Return
from library.Route import route
from service.AuthService import AuthService
from library.Exception import UserException


@route(r"/auth/list")
class AllAuthHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        return AuthService().get_all_auths()


@route(r'/auth/add')
class AddAuthHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        auth = self.post_arguments.get("auth", None)
        name = self.post_arguments.get("name", None)

        if auth is None:
            raise UserException(code=10001, desc="请填写权限点")

        if name is None:
            raise UserException(code=10001, desc="请填写权限点名称")

        return AuthService().add_auth(name=name, auth_code=auth)
