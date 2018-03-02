#!/usr/bin/env python

from sqlalchemy.orm import scoped_session
from library.Exception import CustomException
from library.Result import Result
from library.Utils import Utils
from library.MyRedis import MyRedis


def DI(**kwargs):
    """ 注入装饰 """

    def outer(cls):
        for x in kwargs:
            setattr(cls, x, kwargs.get(x))
        return cls

    return outer


def Singleton(cls):
    """ 单例 """
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


def Transaction(name=None):
    """
    声明式事务,该方法只能使用在对方法上
    特性 :
        a. 支持直接传入session对象(暂无实现)
        b. 传入session对象对应的类书属性名称
    如果出现exception ,直接上抛异常给调用方
    """

    def outer(func):
        def _deco(self, *args, **kwargs):
            if name is not None and hasattr(self, name):
                session = getattr(self, name)
                if isinstance(session, scoped_session):
                    try:
                        res = func(self, *args, **kwargs)
                        session.commit()
                        return res
                    except CustomException as ce:
                        session.rollback()
                        raise CustomException(code=ce.code, desc=ce.msg)
                    except Exception as e:
                        session.rollback()
                        raise e
                    finally:
                        pass
            else:
                print("找不到session对象，无法开启自动事务")

        return _deco

    return outer


def Return(func):
    """
    拦截方法返回，controller 层方法无需再手动编写返回代码
    :return: Result 对象
    """

    def _deco(self, *args, **kwargs):
        res = func(self, *args, **kwargs)
        if not isinstance(res, Result):
            res = Result(code=0, data=res)

        self.json(res)

    return _deco


def Deprecated(func):
    """ 废弃方法装饰器 """

    def _deco(self, *args, **kwargs):
        raise CustomException(code=1003, desc="{path} 已经废弃".format(path=self.request.path))

    return _deco


def Cache(name='redis', time=3000):
    """
    缓存
    """

    def outer(func):
        def _deco(self, *args, **kwargs):
            cache_key = Utils._compute_key(func, args, kwargs)
            if hasattr(self, name):
                cache_obj = getattr(self, name, None)
                if isinstance(cache_obj, MyRedis):
                    data = cache_obj.get(cache_key)
                    if data is None:
                        print("没有命中缓存,执行函数")
                        data = func(self, *args, **kwargs)
                        print("将数据加入到缓存中")
                        cache_obj.setex(cache_key, time, data)
                    else:
                        print("命中缓存")
                else:
                    data = func(self, *args, **kwargs)
            else:
                data = func(self, *args, **kwargs)

            return data

        return _deco

    return outer
