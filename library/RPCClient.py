#!/usr/bin/env python

"""
connect长时间不用会异常，暂时每次使用新连接来解决
"""

from .Decorate import Singleton
from zerorpc import Client
from facebookads import FacebookAdsApi
from facebookads.exceptions import FacebookRequestError


@Singleton
class RPCClient(object):
    def __init__(self, app_id, app_secret, endpoint):
        self.app_id = app_id
        self.app_secret = app_secret
        self.endpoint = endpoint

    def call_old(self, access_token='', method='', path=(), params={}, async=False):
        self.client = Client(heartbeat=60, timeout=60)
        self.client.connect(self.endpoint)
        res = self.client.call(self.app_id, self.app_secret, access_token, method, path, params, async=async)
        self.client.close()
        return res

    def call(self, access_token='', method='', path=(), params={}):
        caller = FacebookAdsApi.init(self.app_id, self.app_secret, access_token)
        try:
            return caller.call(method, path, params).json()
        except FacebookRequestError as fberror:
            return fberror.body()
        except Exception as es:
            raise es


