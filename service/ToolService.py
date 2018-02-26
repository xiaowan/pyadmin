#!/usr/bin/env python

from .BaseService import BaseService
from dao.ToolDAO import ToolDAO
from library.Result import Result


class ToolService(BaseService):
    """ 工具相关的功能 """

    def __init__(self):
        self.toolDAO = ToolDAO.getInstance()
        super().__init__()

    def get_all_db(self):
        """ 查询所有数据库 """
        res = self.toolDAO.get_all_db()
        return Result(code=0, data=res)

    def get_all_tables(self, dbname=""):
        """ 指定数据库的所有表 """
        res = self.toolDAO.get_all_tables(dbname)
        return Result(code=0, data=res)

    def get_schema(self, dbname='', table='', superclass='', prefix="yes"):
        """ 指定数据库和表的schema """
        res = self.toolDAO.get_schema(dbname, table)
        schema = []
        columns = []
        for x in res:
            schema.append({
                'table_name': x['TABLE_NAME'],
                'data_type': x['DATA_TYPE'],
                'is_nullable': x['IS_NULLABLE'].lower(),
                'column_name': x['COLUMN_NAME'],
                'default_value': x['COLUMN_DEFAULT'],
                'extra': x['EXTRA'],
                'column_key': x['COLUMN_KEY'],
            })

            columns.append(x['COLUMN_NAME'])

        data = []
        data.append("#!/usr/bin/env python")
        data.append("\n")
        data.append("from .BaseDO import {superclass}".format(superclass=superclass))
        data.append("from sqlalchemy import Column")
        data.append("from sqlalchemy.types import *")
        data.append("\n")
        data.append("\n")
        data.append("class {name}DO({superclass}):".format(name=self.toolDAO.get_schema_name(table, prefix),
                                                           superclass=superclass))
        data.append("    __tablename__='{table}'".format(table=table))
        data.append("\n")
        fields = []
        if schema:
            for x in schema:
                condition = []
                condition.append(self.toolDAO.get_datatype_mapper(x['data_type']))

                if x['column_key'] == 'PRI':
                    condition.append("primary_key=True")

                if x['extra'] == 'auto_increment':
                    condition.append("autoincrement=True")

                if x['is_nullable'] == 'yes':
                    condition.append("nullable=True")
                else:
                    condition.append("nullable=False")

                if x['default_value']:
                    value = x["default_value"]
                    if x['data_type'] in ('varchar', 'text'):
                        value = "'{value}'".format(value=value)
                    condition.append("default={value}".format(value=value))

                fields.append({
                    "key": x["column_name"],
                    "val": "    {column_name} = Column({condition})".format(column_name=x["column_name"],
                                                                            condition=", ".join(condition))
                })

        return Result(code=0, data={
            "data": data,
            "fields": fields,
            'columns': columns,
        })


