#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib, urllib, config, urllib2, cookielib, db

#登陆使sig生效
def getsig():
    posturl = config.loginurl
    datas = {'name':config.user,'password':config.passwd,'ldap':'0','sig':'','callback':'/'}
    cookies = cookielib.LWPCookieJar()
    data = urllib.urlencode(datas)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
    opener.open(posturl,data)
    for cookie in cookies:
        if cookie.name == 'sig':
            return cookie.value
    return 'error'

#post ping定时任务接口
def addping(des,times,types,hip):
    httpClient = None
    try:
        params = urllib.urlencode({'descriptions[]': des, 'timeout': times, 'type':types, 'hosts[]':hip})
        headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            ,  "Cookie": "sig="+getsig()+""}
        httpClient = httplib.HTTPConnection(config.host, config.port, timeout=30)
        httpClient.request("POST", "/task/ping/create", params, headers)
        response = httpClient.getresponse()
        if response.status == 200:
            return True
        else:
            return False
    except Exception, e:
        print e
        return False
    finally:
        if httpClient:
            httpClient.close()

#post dns/http定时任务接口
def adddns(des,hip,times,types):
    httpClient = None
    try:
        params = urllib.urlencode({'description':des, 'hosts[]':hip, 'timeout':times, 'type':types})
        headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            ,  "Cookie": "sig="+getsig()+""}
        httpClient = httplib.HTTPConnection(config.host, config.port, timeout=30)
        httpClient.request("POST", "/task/create", params, headers)
        response = httpClient.getresponse()
        if response.status == 200:
            return True
        else:
            return False
    except Exception, e:
        print e
        return False
    finally:
        if httpClient:
            httpClient.close()

#post 监控图管理创建任务
def addmonitor(name,host,times,counter,type,aj):
    httpClient = None
    try:
        params = urllib.urlencode({'title':name, 'hosts':host, 'timespan':times, 'counters':counter, 'graph_type':type, 'ajax':aj})
        headers = {"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
            ,  "Cookie": "sig="+getsig()+""}
        httpClient = httplib.HTTPConnection(config.monitorhost, config.monitorport, timeout=30)
        httpClient.request("POST", "/screen/"+str(db.readid())+"/graph", params, headers)
        response = httpClient.getresponse()
        if response.status == 200:
            return True
        else:
            return False
    except Exception, e:
        print e
        return False
    finally:
        if httpClient:
            httpClient.close()








