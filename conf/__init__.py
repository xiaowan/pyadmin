#!/usr/bin/env python

from oslo_config import cfg
from oslo_log import log as logging
from os.path import join, dirname
from os import environ

conf = cfg.CONF
log = logging.getLogger(__name__)
logging.register_options(conf)

# common
default_opts = [
    # cfg.StrOpt(name="debug", default=True),
    cfg.IntOpt(name="port", default=8888),
    cfg.StrOpt(name="env", default="debug"),  # 环境变量值
    cfg.StrOpt(name="environ", default="UNITYMOB_ENVIRON"),  # 环境变量key
]
conf.register_opts(default_opts)
conf.register_cli_opts([
    cfg.IntOpt(name='port', default=8888),
])

# sqlalchemy
sqlalchemy = cfg.OptGroup(name='sqlalchemy', title="MySQL ORM 相关配置")
conf.register_group(sqlalchemy)
conf.register_cli_opts([
    cfg.BoolOpt('echo', default=True),
    cfg.BoolOpt('autoflush', default=True),
    cfg.IntOpt('pool_size', 10),
    cfg.IntOpt('pool_recycle', 3600)
], sqlalchemy)

# mysql
mysql = cfg.OptGroup(name='mysql', title="MySQL DSN配置")
conf.register_group(mysql)
conf.register_cli_opts([
    cfg.StrOpt('unitymob', default='localhost'),
], mysql)

# redis
redis = cfg.OptGroup(name='redis', title="Redis 相关配置")
conf.register_group(redis)
conf.register_cli_opts([
    cfg.StrOpt('host', default='127.0.0.1'),
    cfg.IntOpt('port', default=6379),
    cfg.StrOpt('password', default='unitymob'),
    cfg.StrOpt('prefix', default='unitymob_'),
], redis)

# rabbitmq
rabbitmq = cfg.OptGroup(name='rabbitmq', title="Rabbitmq 相关配置")
conf.register_group(rabbitmq)
conf.register_cli_opts([
    cfg.StrOpt('dsn', default=''),
], rabbitmq)

env = environ.get(conf.environ, 'conf')
env = env if env in ['debug', 'pre', 'conf'] else 'conf'
conf(default_config_files=[join(dirname(__file__), '.'.join([env, 'ini']))])

logging.setup(conf, "unitymob")
