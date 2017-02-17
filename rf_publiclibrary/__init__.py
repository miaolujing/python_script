#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'LiBin'
__mtime__ = '16/6/13'
			  ┏┓   ┏┓
			 ┏┛┻━━━┛┻┓
			 ┃   ☃    ┃
			 ┃ ┳┛  ┗┳  ┃
			 ┃    ┻    ┃
			 ┗━┓      ┏━┛
			  ┃       ┗━━━┓
			  ┃  神兽保佑  ┣┓
			  ┃　永无BUG！ ┏┛
			  ┗┓┓┏━┳┓┏┛
			   ┃┫┫ ┃┫┫
			   ┗┻┛ ┗┻┛
"""
#  Copyright (c) 2010 Franz Allan Valencia See
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from publiclibrary import PublicLibrary
from req import Req


__version__ = '0.1'


class CustomLibrary(PublicLibrary,Req):

    #   这里其实写不写都无所谓，装x而已。

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'