#!/usr/bin/env python

from .BaseService import BaseService
from mapper.UserDO import UserDO
from mapper.UserRoleDO import UserRoleDO
from library.Result import Result
from library.Exception import UserException
from library.Decorate import Transaction
from dao.UserDAO import UserDAO
from dao.AuthDAO import AuthDAO


class UserService(BaseService):
    def __init__(self):
        self.userDAO = UserDAO.getInstance()
        self.authDAO = AuthDAO.getInstance()
        super().__init__()

    def token_key(self, token):
        return self.utils.get_key("token_" + token)

    def get_user_by_token(self, token):
        """ 根据用户token获取用户信息 """
        return self.userDAO.get_user_by_token(self.token_key(token))

    def get_user_by_username(self, username):
        """ 根据用户名获取用户信息 """
        return self.userDAO.get_user_by_username(username)

    @Transaction(name="session")
    def login(self, username=None, password=None):
        """ 判断用户是否允许登陆 """
        user = self.userDAO.get_user_by_username(username)
        try:
            assert user is not None
            if user.is_valid == 'no':
                raise UserException(code=11000)

            if user.password == self.utils.md5(password):
                user.token = self.userDAO.make_token()
                data = user.columnitems
                data['token'] = user.token
                # 获取用的所有角色
                data['roles'] = []
                roles = self.userDAO.get_user_roles(user.id)
                if roles:
                    data['roles'].extend([role.role for role in roles])
                else:
                    raise UserException(11012)
                self.userDAO.update_user_info(user.id, token=user.token)
                # 将token存到redis中
                res = self.redis.setex(self.token_key(user.token), 24 * 60 * 60 * 30, data)
                return Result(code=0, data=data)
            else:
                raise UserException(code=11001)
        except AssertionError as ae:
            raise UserException(code=11002)

    @Transaction(name="session")
    def logout(self, uid=None, token=None):
        if self.redis.delete(self.token_key(token)):
            self.userDAO.update_user_info(uid, token=None)
            return Result(code=0, msg="退出成功")
        else:
            raise UserException(code=11003)

    def get_users(self):
        return self.userDAO.get_users()

    @Transaction(name="session")
    def add_user(self, loginname=None, nickname=None, password=None, is_valid=1):
        """ 添加用户 """
        userinfo = UserService().get_user_by_username(loginname)
        if userinfo:
            raise UserException(code=11011)

        user = UserDO()
        user.loginname = loginname
        user.nickname = nickname
        user.password = self.utils.md5(password)
        user.is_valid = is_valid
        self.userDAO.add_user(user=user)
        return user

    @Transaction(name="session")
    def user_add_roles(self, uid=None, roles=[]):
        """ 给用户新增角色 """
        result = Result()
        objs = []
        if len(roles) > 0:
            for role in roles:
                tmp = UserRoleDO()
                tmp.uid = uid
                tmp.role = role
                objs.append(tmp)
                del tmp
            self.userDAO.add_roles_for_user(objs)
            result.code = 0
        else:
            raise UserException(code=11005)
        return result

    @Transaction(name="session")
    def user_del_roles(self, uid=None, roles=[]):
        """ 用户除去指定角色 """
        if len(roles) > 0:
            self.userDAO.user_del_roles(uid, roles)
            return Result(code=0)
        else:
            raise UserException(11006)

    def get_user_business(self, uid=None):
        """ 获取用户所有所属business """
        return self.userDAO.get_user_business(uid)

    @Transaction(name="session")
    def allow_user_login(self, uid):
        """ 允许指定用户登陆 """
        try:
            self.userDAO.update_user_info(uid, is_valid='yes')
            return Result(code=0)
        except Exception as ex:
            raise UserException(code=11004)

    @Transaction(name="session")
    def forbidden_user_login(self, uid):
        """ 禁止指定用户登陆 """
        try:
            self.userDAO.update_user_info(uid, is_valid='no')
            return Result(code=0)
        except Exception as ex:
            raise UserException(code=11004)

    def get_user_roles(self, uid=None):
        """ 获取指定用户的所有角色 """
        return self.userDAO.get_user_roles(uid)

    def have_power(self, uid=None, auth=None):
        """" 判断用户是否有权限使用该接口 """
        # 用户所有角色
        roles = self.userDAO.get_user_roles(uid)
        roles = [role.role for role in roles]
        # 权限对象
        auth_obj = self.authDAO.get_auth_by_code(auth)
        if not auth_obj:
            raise UserException(code=403, desc="抱歉，您没有 {name} 的使用权限".format(name=auth))

        # 判断该权限是否在角色中
        res = self.authDAO.have_power(roles, auth_obj.id)
        if not res:
            raise UserException(code=403, desc="抱歉，您没有 {name} 功能的使用权限".format(name=auth_obj.name))
