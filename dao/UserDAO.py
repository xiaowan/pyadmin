#!/usr/bin/env python

import uuid
import requests
from sqlalchemy import desc
from .BaseDAO import BaseDAO
from library.Exception import RPCException
from mapper.UserDO import UmUserDO
from mapper.UserRoleDO import UserRoleDO


class UserDAO(BaseDAO):
    """ 用户类相关原子操作 """

    def make_token(self):
        """ 生成访问token """
        return str(uuid.uuid1())

    def get_user_by_username(self, username):
        """ 根据用户名获取用户信息 """
        return self.session.query(UmUserDO).filter(UmUserDO.loginname == username).first()

    def get_user_by_id(self, uid=None):
        """ 根据uid 获取用户 """
        return self.session.query(UmUserDO).filter(UmUserDO.id == uid).first()

    def get_user_by_token(self, token=None):
        """ 根据用户token获取用户信息 """
        return self.redis.get(token)

    def update_user_info(self, uid=None, **kwargs):
        """ 更新用户信息 """
        return self.session.query(UmUserDO).filter(UmUserDO.id == uid).update(kwargs)

    def get_users(self):
        """ 获取用户 """
        return self.session.query(UmUserDO).order_by(desc(UmUserDO.id)).all()

    def add_user(self, user=None):
        """ 批量添加用户 """
        return self.session.add(user)

    def add_roles_for_user(self, roles=[]):
        """ 给用户新增角色 """
        return self.session.add_all(roles)

    def user_del_roles(self, uid=None, roles=[]):
        """ 用户除去指定角色 """
        return self.session.query(UserRoleDO).filter(UserRoleDO.uid == uid). \
            filter(UserRoleDO.role.in_(roles)).delete(synchronize_session=False)

    def get_user_roles(self, uid=None):
        """ 获取指定用户的所有role """
        return self.session.query(UserRoleDO).filter(UserRoleDO.uid == uid).all()

    def save_user_businesses(self, businesses=[]):
        """ 保存用户business信息 """
        return self.session.add_all(businesses)

    def save_applications(self, applications=[]):
        return self.session.add_all(applications)
