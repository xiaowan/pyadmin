#!/usr/bin/env python


from sqlalchemy import desc
from .BaseDAO import BaseDAO
from library.Decorate import Transaction
from mapper.UmPowerDO import UmPowerDO


class PowerDAO(BaseDAO):
    def get_powers(self):
        """ 获取所有的权限列表 """
        return self.session.query(UmPowerDO).order_by(desc(UmPowerDO.id)).all()

    @Transaction(name="session")
    def add_power(self, power=None, name=None, desc=None):
        """ 添加权限 """
        data = UmPowerDO()
        data.power = power
        data.name = name
        data.desc = desc
        self.session.add(data)
        return data
