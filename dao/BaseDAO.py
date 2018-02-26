from library.G import G
from library.Decorate import DI


@DI(g=G())
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

    class ImageType(object):
        carousel = 'Carousel'
        single = 'Single-Image'
        video = 'Video'
