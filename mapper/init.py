#!/usr/bin/env python

from conf import conf
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


sa = conf.sqlalchemy

db_engine = create_engine(conf.mysql.unitymob, echo=sa.echo, pool_size=sa.pool_size, pool_recycle=sa.pool_recycle)
UnitymobSession = sessionmaker(bind=db_engine, autoflush=sa.autoflush)
