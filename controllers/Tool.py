#!/usr/bin/env python

from library.Handlers import BaseHandler
from service.ToolService import ToolService
from library.Exception import CustomException
from library.Route import route
from library.Decorate import Return


@route(r'/tool/dbs')
class AllDbHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        """ 所有数据库 """
        return ToolService().get_all_db()


@route(r'/tool/tables')
class AllTablesHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        """ 所有表 """
        dbname = self.get_argument('dbname', None)
        if not dbname:
            raise CustomException(code=10001, desc="请选择要操作的数据库")

        return ToolService().get_all_tables(dbname)


@route(r'/tool/schema')
class GetSchemaHandler(BaseHandler):
    @Return
    def get(self, *args, **kwargs):
        """ 获取模式 """
        dbname = self.get_argument("dbname", None)
        table = self.get_argument("table", None)
        superclass = self.get_argument("superclass", None)
        prefix = self.get_argument("prefix", "yes")
        if not dbname:
            raise CustomException(code=10001, desc="请选择要操作的数据库")
        if not table:
            raise CustomException(code=10001, desc="请选择要操作的数据表")

        return ToolService().get_schema(dbname, table, superclass, prefix)
