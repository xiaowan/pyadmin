#!/usr/bin/env python


from .BaseDAO import BaseDAO


class ToolDAO(BaseDAO):
    """ 帮助类 """

    def get_all_db(self):
        """ 查询所有数据库 """
        res = self.session.execute("SELECT `SCHEMA_NAME` FROM `information_schema`.`SCHEMATA`").fetchall()
        return [dict(x) for x in res]

    def get_all_tables(self, dbname=""):
        """ 查询指定数据库的所有表 """
        res = self.session.execute("select table_name from information_schema.tables where table_schema= :db_name ",
                                   {'db_name': dbname}).fetchall()
        return [dict(x) for x in res]

    def get_schema(self, dbname=None, table=None):
        """ 指定数据库和表的表结构 """
        res = self.session.execute(
            "SELECT * FROM information_schema.columns WHERE table_schema=:db AND table_name=:table_name",
            {'db': dbname, 'table_name': table}).fetchall()
        return [dict(x) for x in res]

    def get_schema_name(self, table_name, prefix="yes"):
        """ 获取表名 """
        name_list = [x.lower().capitalize() for x in table_name.split("_")]
        if prefix == "no":
            name_list = name_list[1:]
        return "".join(name_list)

    def get_datatype_mapper(self, data_type=None):
        """ 字段到sqlalchemy类型的对应 """
        data_type = data_type.lower()
        res = 'Unknown'
        if data_type == 'int':
            res = 'Integer'
        if data_type == 'varchar':
            res = 'String'
        if data_type == 'bigint':
            res = 'BigInteger'
        if data_type == 'text':
            res = 'Text'
        if data_type == 'tinyint':
            res = 'SmallInteger'
        if data_type == 'float':
            res = 'Float'
        if data_type == 'decimal':
            res = 'DECIMAL'
        if data_type == 'bit':
            res = 'BIT'
        if data_type == 'double':
            res = 'DOUBLE'
        if data_type == 'date':
            res = 'DATE'
        if data_type == 'datetime':
            res = 'DATETIME'
        if data_type == 'timestamp':
            res = 'TIMESTAMP'
        if data_type == 'mediumtext':
            res = 'MEDIUMTEXT'

        return res
