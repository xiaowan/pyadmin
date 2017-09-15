#!/usr/bin/env python

import redis
import pickle
from library.Decorate import Singleton


@Singleton
class MyRedis(object):
    """ redis 单例模块 """
    redis = None

    def __init__(self, host, port, password, decode_responses):
        self.redis = redis.StrictRedis(host=host, port=port, password=password, decode_responses=decode_responses)

    def setex(self, name, time, value):
        return self.redis.setex(name, time, pickle.dumps(value))

    def delete(self, *names):
        return self.redis.delete(*names)

    def get(self, name):
        data = self.redis.get(name)
        try:
            assert data is not None
            return pickle.loads(data)
        except AssertionError as ae:
            return None

