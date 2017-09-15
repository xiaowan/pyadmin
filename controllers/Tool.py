#!/usr/bin/env python


from library.Handlers import BaseHandler
from service.ToolService import ToolService
from library.Exception import CustomException


class AllDbHandler(BaseHandler):
    def get(self, *args, **kwargs):
        res = ToolService().get_all_db()
        self.json(res)


class AllTablesHandler(BaseHandler):
    def get(self, *args, **kwargs):
        dbname = self.get_argument('dbname', None)
        if not dbname:
            raise CustomException(code=10001, desc="请选择要操作的数据库")

        res = ToolService().get_all_tables(dbname)
        self.json(res)


class GetSchemaHandler(BaseHandler):
    def get(self, *args, **kwargs):
        dbname = self.get_argument("dbname", None)
        table = self.get_argument("table", None)
        superclass = self.get_argument("superclass", None)
        prefix = self.get_argument("prefix", "yes")
        if not dbname:
            raise CustomException(code=10001, desc="请选择要操作的数据库")
        if not table:
            raise CustomException(code=10001, desc="请选择要操作的数据表")

        res = ToolService().get_schema(dbname, table, superclass, prefix)
        self.json(res)


route = [
    (r'/tool/dbs', AllDbHandler), # 所有数据库
    (r'/tool/tables', AllTablesHandler), # 所有表
    (r'/tool/schema', GetSchemaHandler), # 获取模式
]