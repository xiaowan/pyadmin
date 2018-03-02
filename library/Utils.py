import json
import time
from decimal import Decimal
from datetime import datetime, date
import hashlib
from conf import conf
import pickle


class Utils(object):
    @staticmethod
    def JSONEncoder():
        class JSONEncoder(json.JSONEncoder):
            """
            Wrapper class to try calling an object's tojson() method. This allows
            us to JSONify objects coming from the ORM. Also handles dates and datetimes.
            """

            def default(self, obj):
                if isinstance(obj, Decimal):
                    return float(obj)
                if isinstance(obj, datetime):
                    return str(obj)
                if isinstance(obj, date):
                    return str(obj)
                try:
                    return obj.tojson()
                except AttributeError:
                    return json.JSONEncoder.default(self, obj)

        return JSONEncoder

    @staticmethod
    def md5(str):
        m2 = hashlib.md5()
        m2.update("{str}".format(str=str).encode("utf-8"))
        return m2.hexdigest()

    @staticmethod
    def _compute_key(function, args, kw):
        key = pickle.dumps((function.__name__, args, kw))
        return hashlib.sha1(key).hexdigest()

    @staticmethod
    def get_key(key):
        """ 拼装 redis key """
        return "{prefix}{key}".format(prefix=conf.redis.prefix, key=key)

    @staticmethod
    def page_start(current_page, page_num):
        """ 计算指定分页的偏移量 """
        current_page = int(current_page) if int(current_page) > 1 else 1
        return (current_page - 1) * page_num

    @staticmethod
    def currentTime(format='%Y-%m-%d %H:%M:%S'):
        return time.strftime(format, time.localtime(int(time.time())))
