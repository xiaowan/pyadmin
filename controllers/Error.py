#!/usr/bin/env python

from tornado.web import  RequestHandler

class NotFoundHandler (RequestHandler):
    def get(self, *args, **kwargs):
        self.write("这里是404页面")

