#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lilian'

import publiclibrary
import requests
import json

publiclibrary = publiclibrary.PublicLibrary()
login_msg = {'email':'miaolj@uyunsoft.cn','passwd':'miaolj161208'}
md5_pwd = publiclibrary.md5(login_msg['passwd'])
login_msg['passwd'] = md5_pwd
headers_login = {'Content-Type': 'application/json','Accept': 'application/json'}
r = requests.post('https://tenant.uyuntest.cn/tenant/api/v1/user/login',data=json.dumps(login_msg), headers=headers_login)
cook = r.cookies
cook_value = ''
for x in cook:
    cook_value +=x.name + '=' + x.value + ';'
cook_value = cook_value[:len(cook_value)-1]