#!/usr/bin/env python

from library.Handlers import BaseHandler
from library.Decorate import Return
from library.Exception import UserException
from library.Route import route
from dao.PowerDAO import PowerDAO


@route(r'/power/list')
class PowerListHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        return PowerDAO().get_powers()


@route(r'/power/add')
class AddPowerHandler(BaseHandler):
    @Return
    def post(self, *args, **kwargs):
        power = self.post_arguments.get("power", None)
        name = self.post_arguments.get("name", None)
        desc = self.post_arguments.get("desc", None)

        if power is None:
            raise UserException(code=10001, desc="请填写权限点")

        if name is None:
            raise UserException(code=10001, desc="请填写权限点名称")

        if desc is None:
            raise UserException(code=10001, desc="请填写权限点描述")

        return PowerDAO().add_power(power, name, desc)
