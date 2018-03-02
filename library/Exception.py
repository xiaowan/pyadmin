#!/usr/bin/env python
"""
自定义异常
"""


class CustomException(Exception):
    """ 自定义异常 """
    """ 这里是通用异常 10000 ~ 10999 """
    error_1001 = '无效TOKEN，请重新登陆'
    error_1002 = 'WARNING: TOKEN NOT FOUND!'
    error_1003 = '该请求已经废弃'
    error_10001 = '参数错误'
    error_10002 = '操作失败'

    def __init__(self, code=None, desc=None):
        self.code = code
        self.desc = desc

    @property
    def msg(self):
        if self.desc is not None:
            return self.desc

        attr = 'error_{code}'.format(code=self.code)
        if hasattr(self, attr):
            return self.__getattribute__(attr)
        else:
            return '未知异常'


class RPCException(CustomException):
    """ 自定义RPC异常类 1500 ~ 2000  """
    error_1500 = 'RPC 调用异常'

    def __init__(self, code=None, desc=None, body=None):
        self.body = body
        super(RPCException, self).__init__(code=code, desc=desc)


class UserException(CustomException):
    """ 用户类异常 11000 ~ 11999 """
    error_11000 = '账号被锁定，暂时无法登陆'
    error_11001 = '密码错误，登陆失败'
    error_11002 = '该用户不存在，请仔细检查登陆名'
    error_11003 = '退出失败'
    error_11004 = '用户状态更新失败'
    error_11005 = '用户角色新增失败'
    error_11006 = '用户角色删除失败'
    error_11011 = '该用户已存在，无法重复添加'
    error_11012 = '该用户未分配角色，暂时无法登陆系统'

class AuthException(CustomException):
    """ 权限类异常 """
    error_12000 = '该权限已经存在，无法重复添加'

class RoleException(CustomException):
    error_13000 = '该角色已经存在，无法添加'