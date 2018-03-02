from sqlalchemy.orm import scoped_session
from mapper.init import UnitymobSession
from conf import conf
from library.MyRedis import MyRedis
from library.MyRabbitmq import MyRabbitmq
from library.RPCClient import RPCClient
from library.Utils import Utils
from tornado.ioloop import IOLoop


class G(object):
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.conf = conf
        self.utils = Utils
        self._session = None

    @property
    def currentIOloopInstance(self):
        return IOLoop.current()

    @property
    def session(self):
        if self._session is None:
            self._session = scoped_session(UnitymobSession)
        return self._session

    @property
    def redis(self):
        return MyRedis.getInstance(host=conf.redis.host, port=conf.redis.port, password=conf.redis.password,
                                   decode_responses=False)

    @property
    def rabbitmq(self):
        """ 自定义rabbitmq """
        return MyRabbitmq.getInstance(conf.rabbitmq.dsn)

    @property
    def rpc(self):
        fb = conf.facebook
        return RPCClient(fb.app_id, fb.app_secret, fb.rpc_endpoint)

    def clear(self):
        """ 释放资源 """
        if self._session is not None:
            self._session.remove()
        self._session = None

        del self.rabbitmq.channel
