#!/usr/bin/env python

import uuid
from .BaseDAO import BaseDAO

from mapper.UserDO import UserDO
from mapper.UserRolesDO import UserRolesDO


class UserDAO(BaseDAO):
    """ 用户类相关原子操作 """
    @staticmethod
    def make_token():
        """ 生成访问token """
        return str(uuid.uuid1())

    def get_user_by_id(self, uid):
        """ 根据id获取用户信息 """
        return self.session.query(UserDO).filter(UserDO.id == uid).first()

    def get_user_by_loginname(self, loginname=None):
        """ 根据登录名获取用户 """
        return self.session.query(UserDO).filter(UserDO.loginname == loginname).first()

    def get_user_by_token(self, token=None):
        """ 根据token获取用户信息 """
        return self.session.query(UserDO).filter(UserDO.token == token).first()

    def update_user(self, user):
        """ 更新用户对象 """
        return self.session.add(user)

    def get_users(self):
        """ 获取所有用户 """
        return self.session.query(UserDO).all()

    def add_user(self, user=None):
        """ 新增用户 """
        self.session.add(user)
        self.session.flush()

    def user_add_role(self, objs = []):
        """ 给用户新增角色 """
        return self.session.add_all(objs)

    def user_del_role(self, uid, roles=[]):
        """ 给用户删除角色 """
        self.session.query(UserRolesDO).filter(UserRolesDO.uid == uid).\
            filter(UserRolesDO.role.in_(roles)).delete(synchronize_session=False)
