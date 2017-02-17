#!/usr/bin/env python
# coding=utf8

import httplib, urllib, json, sys, time, config


def httppost(url, method, isps=[], host="", referer="", cookie="", agent=""):
    httpClient = None
    try:
        params = urllib.urlencode({'param.Url': url, 'param.Isp[]': isps, 'param.Method': method
                                      , 'param.Host': host, 'param.Referer': referer
                                      , 'param.Cookie': cookie, 'param.UserAgent': agent})
        headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            , "Accept": "*/*"}

        httpClient = httplib.HTTPConnection(config.host, config.port, timeout=30)
        httpClient.request("POST", "/s/https", params, headers)

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
        return 0
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


#single isp+get
len1 = httppost("www.baidu.com", "GET", ['y'])
if  len1 < 0:
    print "single isp+get post Fail"
if httpgets(len1) == True:
    print "single isp+get get success"
else:
    print "single isp+get get fail"


#all isp+get
len2 = httppost("www.qq.com", "GET", ['y','d','l','t','c','h','j','f','q'])
if len2 < 0:
    print "all isp+get post Fail"
if httpgets(len2) == True:
    print "all isp+get get success"
else:
    print "all isp+get get fail"


#all param+get
len3 = httppost("kb.qiniu.com", "GET", ['y','d','l','t','c','h','j','f','q'],"kb.qiniu.com","/52pw6cde","123"
        ,"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
if len3 < 0:
    print "all param+get post Fail"
if httpgets(len3) == True:
    print "all param+get get success"
else:
    print "all param+get get fail"


#single isp+head
len4 = httppost("www.baidu.com", "HEAD", ['d'])
if len4 < 0:
    print "single isp+head post Fail"
if httpgets(len4) == True:
    print "single isp+head get success"
else:
    print "single isp+head get fail"


#all isp+head
len5 = httppost("www.qq.com", "HEAD", ['y','d','l','t','c','h','j','f','q'])
if len5 < 0:
    print "all isp+head post Fail"
if httpgets(len5) == True:
    print "all isp+head get success"
else:
    print "all isp+head get fail"


#all param+head
len6 = httppost("kb.qiniu.com", "HEAD", ['y','d','l','t','c','h','j','f','q'],"kb.qiniu.com","/52pw6cde","123"
        ,"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11")
if len6 < 0:
    print "all param+head post Fail"
if httpgets(len6) == True:
    print "all param+head get success"
else:
    print "all param+head get fail"