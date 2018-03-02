#!/usr/bin/env python

from library.Exception import UserException
from library.Handlers import BaseHandler
from library.Result import Result
from library.Decorate import Return
from library.Route import route
from service.UserService import UserService


@route(r"/user/login")
class UserLoginHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        username = self.post_arguments.get("username", None)
        password = self.post_arguments.get("password", None)
        return UserService().login(username, password)


@route(r"/user/logout")
class UserLogoutHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        return UserService().logout(self.uid, self.token)


@route(r"/user/info")
class UserInfoHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        return UserService().get_user_by_token(self.token)


@route(r"/user/list")
class UserListHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        return UserService().get_users()


@route(r"/user/forbid")
class ForbidUserHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        user_id = self.post_arguments.get("uid", None)
        if user_id is None:
            raise UserException(code=10001, desc="请传入需要操作的用户id")

        return UserService().forbidden_user_login(user_id)


@route(r"/user/allow")
class AllowUserHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        user_id = self.post_arguments.get("uid", None)
        if user_id is None:
            raise UserException(code=10001, desc="请传入需要操作的用户id")
        return UserService().allow_user_login(user_id)


@route(r"/user/add")
class AddUserHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        loginname = self.post_arguments.get("loginname", None)
        nickname = self.post_arguments.get("nickname", None)
        password = self.post_arguments.get("password", None)
        checkPass = self.post_arguments.get("checkPass", None)
        is_valid = self.post_arguments.get("is_valid", None)
        if loginname is None:
            raise UserException(code=10001, desc="loginname不能为空")

        if nickname is None:
            raise UserException(code=10001, desc="nickname不能为空")
        if password is None:
            raise UserException(code=10001, desc="密码不能为空")
        if password != checkPass:
            raise UserException(code=10001, desc="两次密码不一致")

        UserService().add_user(
            loginname=loginname,
            nickname=nickname,
            password=password,
            is_valid=is_valid
        )
        return Result(code=0)


@route(r"/user/role/add")
class AddRoleForUserHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        uid = self.post_arguments.get("uid", None)
        roles = self.post_arguments.get("roles", None)
        return UserService().user_add_roles(uid, roles)


@route(r"/user/role/del")
class DelRoleForUserHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        uid = self.post_arguments.get("uid", None)
        roles = self.post_arguments.get("roles", None)
        return UserService().user_del_roles(uid, roles)


@route(r"/user/roles")
class GetUserRoleHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        uid = self.get_argument("uid", default=None)
        return UserService().get_user_roles(uid)
