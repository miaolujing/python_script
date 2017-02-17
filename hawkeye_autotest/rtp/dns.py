#!/usr/bin/env python
# coding=utf8

import httplib, urllib, json, sys, time, config


def httppost(url, isps=[]):
    httpClient = None
    try:
        params = urllib.urlencode({'param.Url': url, 'param.Isp[]': isps})
        headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            , "Accept": "*/*"}

        httpClient = httplib.HTTPConnection(config.host, config.port, timeout=30)
        httpClient.request("POST", "/s/dns", params, headers)

        response = httpClient.getresponse()
        data = response.read()
        if response.status == 200:
            return decode(data)
        else:
            return -1
    except Exception, e:
        print e
        return -1
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
        return len(ss.Isp)
    except Exception, e:
        print e
    return -1


def decodeget(data):
    try:
        ss = json.loads(data, object_hook=JSONObject)
        if ss.succ == True and ss.msg == "success":
            return len(ss.data)
    except Exception, e:
        print e
    return -1


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
        return -1
    finally:
        if httpClient:
            httpClient.close()


def httpgets(length):
    #httpget()
    tries = 10
    while tries > 0:
        length = length - httpget()
        if length == 0:
            return True
        tries = tries - 1
        time.sleep(3)
    return False


#single isp
len1 = httppost("www.baidu.com", ['d'])
if len1 < 0:
    print "single isp post Fail"
if httpgets(len1) == True:
    print "single isp get success"
else:
    print "single isp get fail"


#all isp
len2 = httppost("www.qq.com",['y','d','l','t','c','h','j','f','q'])
if len2 < 0:
    print "all isp post Fail"
if httpgets(len2) == True:
    print "all isp get success"
else:
    print "all isp get fail"
