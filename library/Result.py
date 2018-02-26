#!/usr/bin/env python
"""
返回结果类
"""


class Result(object):
    __slots__ = ("code", "msg", "data")

    def __init__(self, code=0, msg="", data=None):
        self.code = code
        self.msg = msg
        self.data = data

    def json(self):
        return {
            "code": self.code,
            "msg": self.msg,
            "data": self.data
        }
