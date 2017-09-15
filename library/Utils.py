
import json
from decimal import Decimal
from datetime import datetime
import hashlib


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
                try:
                    return obj.dict
                except AttributeError:
                    return json.JSONEncoder.default(self, obj)
        return JSONEncoder

    @staticmethod
    def md5(str):
        m2 = hashlib.md5()
        m2.update("{str}".format(str=str).encode("utf-8"))
        return m2.hexdigest()
