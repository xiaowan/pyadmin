#!/usr/bin/env python

class Route(object):
    def __init__(self):
        self.url_list = list()

    def get_urls(self):
        """ 获取所有的urls """
        return self.url_list

    def __call__(self, _url, name=None):
        def _(cls):
            self.url_list.append((_url, cls))

            return cls

        return _


route = Route()
