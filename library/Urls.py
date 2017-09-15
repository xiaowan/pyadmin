#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controllers import User
from controllers import Tool
from controllers import Role
from controllers import Auth

urls = []
urls.extend(User.route)
urls.extend(Tool.route)
urls.extend(Role.route)
urls.extend(Auth.route)


