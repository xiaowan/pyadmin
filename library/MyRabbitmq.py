#!/usr/bin/env python

"""
自定义rabbitmq
"""

import pika
import json


class MyRabbitmq( object ):
    _instance = None
    _connection = None
    _channel = None

    @classmethod
    def getInstance(cls, dsn):
        if cls._instance is None:
            cls._instance = cls(dsn)
        return cls._instance

    def __init__(self, dsn):
        self.dsn=dsn

    @property
    def connection(self):
        if self._connection is None:
            self._connection = pika.BlockingConnection(pika.URLParameters(self.dsn))
        return self._connection

    @property
    def channel(self):
        if self._channel is None:
            self._channel = self.connection.channel()
        return self._channel

    @channel.deleter
    def channel(self):
        if self._channel is not None:
            self._channel.close()
        self._channel = None

    def publish(self, exchange=None, routing_key=None, message={}):
        """ 发布消息 """
        return self.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=json.dumps(message))

    def close(self):
        """ 关闭连接 """
        self.connection.close()
