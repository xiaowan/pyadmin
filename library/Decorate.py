
from sqlalchemy.orm import scoped_session
from library.Exception import CustomException


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
                    try :
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

