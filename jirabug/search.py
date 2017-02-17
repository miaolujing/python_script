#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lilian'

import config,urllib,urllib2,cookielib,json,sys,requests,gettime

#强制utf-8
# reload(sys)
# sys.setdefaultencoding('utf-8')

#获取cookies
def getcookies():
    posturl = config.loginurl
    datas = {"os_username": config.username, "os_password": config.passwd, "os_destination": "", "user_role": "", "atl_token": "", "login": "登录"}
    cookies = cookielib.LWPCookieJar()
    data = urllib.urlencode(datas)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
    opener.open(posturl,data)
    for cookie in cookies:
        if cookie.name == 'JSESSIONID':
            return cookie.value
    return 'error'

#post bug接口
def postsearch(type):
    jql = "project = SHOW AND issuetype in (Bug, 子BUG) AND created >= " + gettime.gettime(
        'start') + " AND created <= " + gettime.gettime('end') + " ORDER BY assignee"
    payload = json.dumps({"jql": jql,"maxResults": config.maxResults})
    headers = {'content-type': "application/json",'cookie': "JSESSIONID="+getcookies()+"",'cache-control': "no-cache"}
    response = requests.post(config.searchurl,data=payload, headers=headers)
    data = response.content
    if type == 'count':
        return count(data)
    if type == 'kind':
        return kind(data)

#解析总数
def count(data):
    try:
        ss = json.loads(data)
        dic = {}
        r1 = []
        r2 = []
        for i in range(0,len(ss['issues'])):
            arr =ss['issues'][i]['fields']['assignee']['displayName']
            r1.append(arr)
        for item in r1:
            dic[item] = dic.get(item, 0) + 1
        for (k,v) in dic.items():
            dict = {}
            dict['count'] = v
            dict['name'] = k
            r2.append(dict)
        return json.dumps(r2,encoding="UTF-8",ensure_ascii=False)
    except Exception, e:
        print e
    return -1

#解析分类总数
class pair:
    def __init__(self,name,level):
        self.name = name
        self.level = level
    def __hash__(self):
        return hash((self.name, self.level))
    def __eq__(self, other):
        return (self.name,self.level) == (other.name, other.level)
    def __ne__(self, other):
        return not(self == other)

def kind(data):
    try:
        ss = json.loads(data)
        dic = {}
        r1 = []
        r2 = []
        for i in range(0,len(ss['issues'])):
            name = ss['issues'][i]['fields']['assignee']['displayName']
            level = ss['issues'][i]['fields']['priority']['name']
            key = pair(name,level)
            r1.append(key)
        for item in r1:
            dic[item] = dic.get(item, 0) + 1
        for (k,v) in dic.items():
            dict = {}
            dict['count'] = v
            dict['name'] = k.name
            dict['level'] = k.level
            r2.append(dict)
        return json.dumps(r2,encoding="UTF-8",ensure_ascii=False)
    except Exception, e:
        print e
    return -1

#post 需求总数
def postepic(type):
    jql1 = "project = SHOW AND issuetype in " \
           "(Epic, 任务, Improvement, 'New Feature', 用户体验, 需求, Sub-Feature, Sub-Improvement, Sub-task, 子需求) " \
           "AND status in (Resolved, Closed) AND updated >= " + gettime.gettime('start') + " AND updated <= " + gettime.gettime(
        'end') + ""
    payload = json.dumps({"jql": jql1, "maxResults": config.maxResults})
    headers = {'content-type': "application/json", 'cookie': "JSESSIONID=" + getcookies() + "",
               'cache-control': "no-cache"}
    response = requests.post(config.searchurl, data=payload, headers=headers)
    data = response.content
    if type == 'fixed':
        return count(data)
