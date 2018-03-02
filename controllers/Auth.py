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


@route(r'/auth/canassign')
class AuthCanAssignHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        """ 可以被分配给角色的权限 """
        return AuthService().get_assign_for_role()


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


@route(r"/auth/newauths")
class NewAuthsHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        return AuthService().get_new_auths()
