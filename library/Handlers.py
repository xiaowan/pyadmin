#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

from oslo_context import context
from tornado.web import RequestHandler
from library.Exception import CustomException
from library.G import G
from library.Result import Result
from library.Utils import Utils
from service.UserService import UserService


class BaseHandler(RequestHandler):
    uid = None
    token = None

    def __init__(self, application, request, **kwargs):
        context.RequestContext()
        self.post_arguments = {}
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def compute_etag(self):
        """ 取消缓存 """
        return None

    def prepare(self):
        if self.request.method == 'OPTIONS':
            return self.options()

        if self.request.path not in ["/user/login"]:
            token = self.request.headers.get("X-Token", None)
            try:
                assert token is not None
                data = UserService().get_user_by_token(token)
                if data is not None:
                    self.uid = data['id']
                    self.token = token
                else:
                    raise CustomException(code=1001)

                UserService().have_power(self.uid, self.request.path)

            except AssertionError as ae:
                raise CustomException(code=1002)

        try:
            self.post_arguments = json.loads(self.request.body.decode('utf-8'))
        except Exception as ex:
            pass

    def write_error(self, status_code, **kwargs):
        if isinstance(kwargs.get('exc_info')[1], CustomException):
            ce = kwargs.get('exc_info')[1]
            self.set_status(200)
            return self.json(Result(code=ce.code, msg=ce.msg))
        else:
            return self.json(Result(code=status_code, msg="未知错误"))

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers",
                        "X-Token, Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def on_finish(self):
        """ 清理资源 """
        G.getInstance().clear()

    def json(self, result):
        self.write(json.dumps(result.json(), cls=Utils.JSONEncoder(), sort_keys=False))
        self.finish()

    def options(self, *args, **kwargs):
        self.set_status(204)
