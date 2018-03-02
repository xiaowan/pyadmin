from library.G import G
from library.Decorate import DI


@DI(g=G.getInstance())
class BaseDAO():
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def conf(self):
        return self.g.conf

    @property
    def utils(self):
        return self.g.utils

    @property
    def redis(self):
        return self.g.redis

    @property
    def session(self):
        return self.g.session

    @property
    def jolly_session(self):
        return self.g.jolly_session

    @property
    def rpc(self):
        return self.g.rpc

    def save(self, obj):
        """ 保存对象，支持批量写入"""
        if isinstance(obj, list):
            res = self.session.add_all(obj)
        else:
            res = self.session.add(obj)
        self.session.flush()
        return res
