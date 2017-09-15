#!/usr/bin/env python

from library.Handlers import BaseHandler
from library.Result import Result
from service.UserService import UserService


class UserLoginHandler(BaseHandler):

    def post(self, *args, **kwargs):
        loginname = self.post_arguments.get("loginname", None)
        password = self.post_arguments.get("password", None)
        result = UserService().login(loginname, password)
        return self.json(result)


class UserLogoutHandler(BaseHandler):
    def post(self, *args, **kwargs):
        #return self.json(UserService().logout(self.uid, self.token))
        return self.json(Result(code=0))


class MeInfoHandler(BaseHandler):
    def get(self, *args, **kwargs):
        userinfo = UserService().get_user_by_token(self.token)
        return self.json(Result(code=0, data=userinfo))


class UserInfoHandler(BaseHandler):
    def get(self, *args, **kwargs):
        uid = self.get_argument('uid')
        res = UserService().get_user_info(uid)
        self.json(res)


class UserListHandler(BaseHandler):
    def get(self, *args, **kwargs):
        res = UserService().get_user_list()
        self.json(res)


class AddUserHandler(BaseHandler):
    def post(self, *args, **kwargs):
        user = self.post_arguments.get('user', None)
        print(user)
        res = UserService().add_user(user)
        self.json(res)


class ForbiddenHandler(BaseHandler):
    def post(self, *args, **kwargs):
        uid = self.post_arguments.get('uid', None)
        res = UserService().forbidden_user(uid)
        self.json(res)


class AllowHandler(BaseHandler):
    def post(self, *args, **kwargs):
        uid = self.post_arguments.get('uid', None)
        res = UserService().allow_user(uid)
        self.json(res)


class UserAddRoleHandler(BaseHandler):
    def post(self, *args, **kwargs):
        uid = self.post_arguments.get('uid', None)
        roles = self.post_arguments.get('roles', [])
        res = UserService().user_add_role(uid, roles)
        self.json(res)


class UserDelRoleHandler(BaseHandler):
    def post(self, *args, **kwargs):
        uid = self.post_arguments.get('uid', None)
        roles = self.post_arguments.get('roles', [])
        res = UserService().user_del_role(uid, roles)
        self.json(res)


route = [
    (r"/user/login", UserLoginHandler),
    (r"/user/me", MeInfoHandler),
    (r"/user/info", UserInfoHandler), # 获取用户信息
    (r"/user/logout", UserLogoutHandler),
    (r"/user/list", UserListHandler),
    (r"/user/add", AddUserHandler),
    (r"/user/forbidden", ForbiddenHandler), # 禁止登陆
    (r"/user/allow", AllowHandler), # 允许登陆
    (r"/user/role/add", UserAddRoleHandler), # 给用户新增角色
    (r"/user/role/del", UserDelRoleHandler), # 给用户删除角色
]

