#!/usr/bin/env python
# coding=utf8

import httplib, urllib, json, time, config


def httppost(params):
    httpClient = None
    try:
        headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            , "Accept": "*/*"}

        httpClient = httplib.HTTPConnection(config.host, config.port, timeout=30)
        httpClient.request("POST", "/s/traceroute", params, headers)

        response = httpClient.getresponse()
        data = response.read()
        if response.status == 200:
            return decode(data)
        else:
            return False
    except Exception, e:
        print e
        return False
    finally:
        if httpClient:
            httpClient.close()


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


def decode(data):
    try:
        ss = json.loads(data, object_hook=JSONObject)
        global uuid
        uuid = ss.uuid
    except Exception, e:
        print e
        return False
    return True


def decodeget(data):
    try:
        ss = json.loads(data, object_hook=JSONObject)
        if ss.succ == True and ss.msg == "success":
            return len(ss.data)
    except Exception, e:
        print e
    return 0


def httpget():
    httpClient = None

    try:
        httpClient = httplib.HTTPConnection(config.host, config.port, timeout=30)
        httpClient.request('GET', '/s/getResult?uuid=' + uuid)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        data = response.read()
        return decodeget(data)
    except Exception, e:
        print e
        return False
    finally:
        if httpClient:
            httpClient.close()


def httpgets(num):
    #httpget()
    tries = 20
    while tries > 0:
        num = num - httpget()
        if num == 0:
            return True
        tries = tries - 1
        time.sleep(3)
    return False


#three isp
if httppost("param.Url=www.baidu.com&param.Isp%5B%5D=1000005&param.Isp%5B%5D=1000001&param.Isp%5B%5D=1000004") == False:
    print "three isp post Fail"
if httpgets(3) == True:
    print "three isp success"
else:
    print "three isp fail"


#single isp
if httppost("param.Url=www.qq.com&param.Isp%5B%5D=1000001") == False:
    print "single isp post Fail"
if httpgets(1) == True:
    print "single isp success"
else:
    print "single isp fail"