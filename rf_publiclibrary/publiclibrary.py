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

#   Licensed under the MIT licence:
#
#   Permission is hereby granted, free of charge, to any person
#   obtaining a copy of this software and associated documentation
#   files (the "Software"), to deal in the Software without
#   restriction, including without limitation the rights to use,
#   copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following
#   conditions:
#
#   The above copyright notice and this permission notice shall be
#   included in all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#   OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#   NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#   HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#   WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#   OTHER DEALINGS IN THE SOFTWARE.


import json
import requests
import time
import hashlib
import random
import pymysql
import redis
import uuid

try:
    from requests.packages.urllib3.exceptions import (
        SNIMissingWarning,
        InsecureRequestWarning,
        InsecurePlatformWarning
    )

# Not show warings
    requests.packages.urllib3.disable_warnings(SNIMissingWarning)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
except ImportError:
    pass


__version__ = '0.1'


class PublicLibrary(object):

    def __init__(self):
        pass

    def data_compare(self, db_data, re_data):
        u"""接收数据库查询数据和接口返回数据返回比对结果,例
         | data compare                   | db_data,re_data                 |
        """
        db_len = len(db_data)
        re_len = len(re_data)
        if db_len != re_len:
            return False

        temp_db = []
        temp_re = []
        for each_db in db_data:
            temp_db.append(list(each_db))
        for each_re in re_data:
            temp_re.append(each_re.values())

        temp_db = sorted(temp_db)
        temp_re = sorted(temp_re)

        # 取差集,暂时用不到
        # for i in range(db_len):
        #     flag = len(set(temp_db[i]).difference(set(temp_re[i])))
        #     if flag:
        #         return False
        if temp_db != temp_re:
            return False
        return True

    def eval_dict(self, strInput):
        u"""接收字符串直接转成需要类型,例
         | eval dict                   | str                |
        """
        strInput = eval(strInput)
        return strInput

    def getCoding(self, strInput):
        u"""
        获取编码格式
        """
        if isinstance(strInput, unicode):
            return "unicode"
        try:
            strInput.decode("utf8")
            return 'utf8'
        except:
            pass
        try:
            strInput.decode("gbk")
            return 'gbk'
        except:
            pass

    def tran2UTF8(self, strInput):
        """
        转化为utf8格式
        """
        strCodingFmt = self.getCoding(strInput)
        if strCodingFmt == "utf8":
            return strInput
        elif strCodingFmt == "unicode":
            return strInput.encode("utf8")
        elif strCodingFmt == "gbk":
            return strInput.decode("gbk").encode("utf8")

    def tran2GBK(self, strInput):
        """
        转化为gbk格式
        """
        strCodingFmt = self.getCoding(strInput)
        if strCodingFmt == "gbk":
            return strInput
        elif strCodingFmt == "unicode":
            return strInput.encode("gbk")
        elif strCodingFmt == "utf8":
            return strInput.decode("utf8").encode("gbk")

    def random_email(self):
        """
        随机生成邮箱
        """
        time_now = str(int(time.time()))
        timestamp = ''.join(random.sample(time_now, 10))
        email = 'libin{0}@uyunsoft.cn'.format(timestamp)

        return email

    def random_mobile(self):
        """
        随机生成手机号
        """
        mobile = '158'
        for i in random.sample(range(10), 8):
            mobile += ''.join(str(i))

        return mobile

    def md5(self, init_str):
        """
        md5加密
        """
        m = hashlib.md5()
        m.update(init_str)
        return m.hexdigest()

    def random_num(self, num):
        """
        随机出给出数字位数的数字
        """
        number = ''
        for i in random.sample(range(10), int(num)):
            number += ''.join(str(i))

        return number

    def time_stamp(self, s_time):
        s_time = str(s_time)
        s_time = s_time.replace('T', ' ')
        s_time = s_time.replace('+0800', '')
        timeArray = time.strptime(s_time, '%Y-%m-%d %H:%M:%S')
        timestamp = int(time.mktime(timeArray))

        return timestamp

    def req(
        self,
        login_msg,
        url,
        method,
        data=None,
        params=None,
        headers=None,
        type=1
    ):
        u"""show专用,有登录状态,例
         | run interface test tenant  | login_msg,url,method,data,headers
        """
        session = requests.Session()
        url = self.tran2UTF8(url)
        method = self.tran2UTF8(method)
        if login_msg:
            login_msg = self.eval_dict(login_msg)
            md5_pwd = self.md5(login_msg['passwd'])
            login_msg['passwd'] = md5_pwd
        if data and type == 1:
            data = self.eval_dict(data)

        headers_login = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        results = 'connection error'
        # 先登录
        r = session.post('https://tenant.uyuntest.cn/tenant/api/v1/user/login',
                         data=json.dumps(login_msg), headers=headers_login)
        print "*******************************"
        print u"登录状态信息"
        print r.status_code
        print r.content
        print "*******************************"
        if headers:
            headers = self.eval_dict(headers)
            session.headers.update(headers)
        else:
            headers = headers_login
        try:
            if method == "post":
                if isinstance(data, dict):
                    data = json.dumps(data)
                results = session.post(
                    url,
                    data=data,
                    params=params,
                    headers=headers,
                    verify=False)
            elif method == "get":
                results = session.get(
                    url, params=data, headers=headers, verify=False)
            elif method == 'delete':
                results = session.delete(url, headers=headers, verify=False)
            elif method == 'put':
                if isinstance(data, dict):
                    data = json.dumps(data)
                results = session.put(
                    url, data=data, headers=headers, verify=False)

            return results
        except requests.ConnectionError as e:
            return e

    def get_errcode(
        self,
        login_msg,
        url,
        method,
        data=None,
        params=None,
        headers=None,
        type=1
    ):
        u"""show专用,有登录状态,例
         | run interface test tenant  | login_msg,url,method,data,headers
        """
        session = requests.Session()
        url = self.tran2UTF8(url)
        method = self.tran2UTF8(method)
        if login_msg:
            login_msg = self.eval_dict(login_msg)
            md5_pwd = self.md5(login_msg['passwd'])
            login_msg['passwd'] = md5_pwd
        if data and type == 1:
            data = self.eval_dict(data)

        headers_login = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        results = 'connection error'
        # 先登录
        r = session.post('https://tenant.uyuntest.cn/tenant/api/v1/user/login',
                         data=json.dumps(login_msg), headers=headers_login)
        print "*******************************"
        print u"登录状态信息"
        print r.status_code
        print r.content
        print "*******************************"
        if headers:
            headers = self.eval_dict(headers)
            session.headers.update(headers)
        else:
            headers = headers_login
        try:
            if method == "post":
                if isinstance(data, dict):
                    data = json.dumps(data)
                results = session.post(
                    url,
                    data=data,
                    params=params,
                    headers=headers,
                    verify=False)
            elif method == "get":
                results = session.get(
                    url, params=data, headers=headers, verify=False)
            elif method == 'delete':
                results = session.delete(url, headers=headers, verify=False)
            elif method == 'put':
                if isinstance(data, dict):
                    data = json.dumps(data)
                results = session.put(
                    url, data=data, headers=headers, verify=False)

            return json.loads(results.content)['errCode']
        except requests.ConnectionError as e:
            return e

    def con_db(self, sql, type=1):
        if type == 1:
            db = pymysql.connect(
                host="10.1.53.249",
                user="uyun_show",
                passwd="uyunShow123!",
                db="uyun_show",
                charset='utf8',
            )
        else:
            db = pymysql.connect(
                host="10.1.53.249",
                user="uyun_show",
                passwd="uyunShow123!",
                db="uyun_show",
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        db.close()
        if type == 1:
            return data[0]
        else:
            return data

    def makeup_windowall_data(self):
        data = self.con_db(
            "select * from window_wall where tenant_id='cad9c8fc5bcd4a97b527ea378f25ecb8'",
            2)
        results = {
            "wallSetting": {
                "title": data.get('title'),
                "titleSize": data.get('title_size'),
                "titleColor": data.get('title_color'),
                "titleColorOpacity": data.get('title_color_opacity')
            },
            "bgSetting": {
                "bgType": data.get('bg_type'),
                "bgColor": data.get('bg_color'),
                "bgColorOpacity": data.get('bg_color_opacity'),
                "bg": data.get('bg')
            },
            "windowSetting": {
                "textSize": data.get('text_size'),
                "textColor": data.get('text_color'),
                "textColorOpacity": data.get('text_color_opacity')
            }
        }
        return results

    def groupdict(self, data):
        data = str(data)
        data = eval(data.replace('null', 'None'))
        result = {}
        for i in range(len(data)):
            for k, v in data[i].items():
                if k == 'groupId':
                    result.setdefault('groupid%s' % (i + 1), v)
        return result

    # web热图保存接口，由于图片bash64编码数据量较大，故而特殊处理
    def heatmap_save(self):
        response = self.req(
            login_msg="{'email': 'demo@uyunsoft.cn','passwd': 'demo'}",
            url='https://web.uyuntest.cn/web/frontApi/v1/heatMap/save',
            method='post',
            data=self.heatmap_data,
            headers="{'Content-Type': 'text/plain;charset=UTF-8'}",
            type=0,
        )
        return response

    def generate_int(self, num):
        lists = ''
        data = '123456789'
        for i in random.sample(data, int(num)):
            lists += ''.join(str(i))
        return lists

    def generate_str(self, num):
        lists = ''
        data = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        for i in random.sample(data, int(num)):
            lists += ''.join(str(i))
        return lists

    # 获取当天时间零点时间戳
    def getTimeOClockOfToday(self):
        t = time.localtime(time.time())
        time1 = time.mktime(
            time.strptime(
                time.strftime(
                    '%Y-%m-%d 00:00:00',
                    t),
                '%Y-%m-%d %H:%M:%S'))
        return long(time1) * 1000

    def get_redis_user(self, platform):
        timestamp = self.getTimeOClockOfToday()
        appid = {'pc': 'TJVnwGhfrgPJp7rzsapPlVB8MRaVkjgU',
                 'android': 'AeuVRKS1HdpnkYH6SeqaEWwxCJacrG91'}
        key = 'overview:%s:%s:%s:province' % (
            platform, timestamp, appid[platform])
        r = redis.Redis(
            host='10.1.53.244',
            password='uyuntestredis',
            port=6379,
            db=1)
        data = r.hgetall(key)
        return data

    #show 判断数据集field_set数据
    def check_field(self,dbdata, getdata):
        for i in range(0, len(dbdata)):
            if dbdata[i][0] == getdata[i]['fieldName'] and dbdata[i][1] == getdata[i]['displayName']:
                return "suss"
            else:
                return "fail"

    #show 判断所有数据源数据
    def check_datasource(self,dbdata, getdata):
        for i in range(0, len(dbdata)):
            if dbdata[i][0] == getdata[i]['id'] and dbdata[i][1] == getdata[i]['name']:
                return "suss"
            else:
                return "fail"

    #获取需要多个字段数据
    def field_db(self,sql):
        db = pymysql.connect(
            host="10.1.53.249",
            user="uyun_show",
            passwd="uyunShow123!",
            db="uyun_show",
            charset='utf8',
        )
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print results
        data = []
        for i in range(0, len(results)):
            data.append(results[i])
        return data
        db.close()

    #show保存部件生成前端uuid
    def fuuid(self):
        return uuid.uuid1().hex

    #show部件大小随机数
    def size_random(self):
        return random.randint(25, 40)

    #show部件位置随机数
    def site_random(self):
        return random.randint(1, 20)

    #删除查询数据库为空，返回0
    def empty_db(self,sql):
        db = pymysql.connect(
            host="10.1.53.249",
            user="uyun_show",
            passwd="uyunShow123!",
            db="uyun_show",
            charset='utf8',
        )
        cursor = db.cursor()
        cursor.execute(sql)
        return cursor.rowcount

if __name__ == '__main__':
    pass
