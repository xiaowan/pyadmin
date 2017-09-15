#!/usr/bin/env python

from .BaseService import BaseService
from library.Result import Result
from library.Exception import UserException
from library.Decorate import Transaction
from dao.UserDAO import UserDAO
from dao.RoleDAO import RoleDAO
from dao.AuthDAO import AuthDAO

from mapper.UserDO import UserDO
from mapper.UserRolesDO import UserRolesDO


class UserService(BaseService):

    def __init__(self):
        self.userDAO = UserDAO.getInstance()
        self.roleDAO = RoleDAO.getInstance()
        self.authDAO = AuthDAO.getInstance()
        super().__init__()

    def token_key(self, token):
        return self.utils.get_key( "token_" + token )

    def get_user_by_token(self, token):
        """ 根据用户token获取用户信息 """
        info = self.userDAO.get_user_by_token(token)
        info = info.dict
        roles = self.roleDAO.get_user_roles(info['id'])
        info['role'] = [role.role for role in roles]

        return info

    @Transaction(name="session")
    def login(self, loginname=None, password=None):
        """ 用户登陆操作 """
        user = self.userDAO.get_user_by_loginname(loginname)
        try:
            assert user is not None
            if user.is_valid == 'no':
                raise UserException(code=11000)
            if user.password == self.utils.md5(password):
                user.token = self.userDAO.make_token()
                self.userDAO.update_user(user)
                return Result(code=0,data=user)
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

    def get_user_list(self):
        """ 获取所有用户 """
        res = self.userDAO.get_users()
        return Result(code=0, data=res)

    @Transaction(name="session")
    def add_user(self, user):
        """ 新增用户 """
        obj = UserDO()
        obj.nickname = user.get('nickname')
        obj.loginname = user.get('loginname')
        obj.password = self.utils.md5(user.get('password'))
        obj.is_valid = 'yes'
        self.userDAO.add_user(obj)

        return Result(code=0)

    @Transaction(name="session")
    def forbidden_user(self, uid):
        """ 禁止用户登陆 """
        user = self.userDAO.get_user_by_id(uid)
        user.is_valid = 'no'
        self.userDAO.update_user(user)
        return Result(code=0)

    @Transaction(name="session")
    def allow_user(self, uid):
        """ 允许用户登陆 """
        user = self.userDAO.get_user_by_id(uid)
        user.is_valid = 'yes'
        self.userDAO.update_user(user)
        return Result(code=0)

    def get_user_info(self, uid):
        """ 获取用户信息 """
        info = self.userDAO.get_user_by_id(uid)
        info = info.dict
        roles = self.roleDAO.get_user_roles(info['id'])
        info['role'] = [role.role for role in roles]
        return Result(code=0, data=info)

    @Transaction(name="session")
    def user_add_role(self, uid, roles=[]):
        """ 给用户新增角色 """
        objs = []
        if roles:
            for x in roles:
                tmp = UserRolesDO()
                tmp.uid = uid
                tmp.role = x
                objs.append(tmp)
                del tmp
            self.userDAO.user_add_role(objs)
        return Result(code=0)

    @Transaction(name="session")
    def user_del_role(self, uid, roles=[]):
        """ 给用户删除角色 """
        self.userDAO.user_del_role(uid, roles)
        return Result(code=0)

    def have_power(self, uid=None, auth=None):
        """" 判断用户是否有权限使用该接口 """
        # 用户所有角色
        roles = self.roleDAO.get_user_roles(uid)
        roles = [role.role for role in roles]
        # 权限对象
        auth_obj = self.authDAO.get_auth_by_code(auth)
        if not auth_obj:
            raise UserException(code=403, desc="抱歉，您没有 {name} 的使用权限".format(name=auth))

        # 判断该权限是否在角色中
        res = self.authDAO.have_power(roles, auth_obj.id)
        if not res:
            raise UserException(code=403, desc="抱歉，您没有 {name} 功能的使用权限".format(name=auth_obj.name))
