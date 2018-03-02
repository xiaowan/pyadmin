#!/usr/bin/env python

from library.Decorate import DI
from library.G import G


@DI(g=G.getInstance())
class BaseService(object):
    @property
    def session(self):
        return self.g.session

    @property
    def utils(self):
        return self.g.utils

    @property
    def redis(self):
        return self.g.redis

    @property
    def rpc(self):
        return self.g.rpc

    @property
    def conf(self):
        return self.g.conf

    @property
    def rabbitmq(self):
        return self.g.rabbitmq
