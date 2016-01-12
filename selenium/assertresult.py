#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, config, db, json, os

#解析ip管理页面结果
def httpget():
    req = urllib2.Request(config.hportal_ips + config.ip + "&mine=1")
    try:
        response = urllib2.urlopen(req)
        data = response.read()
        print data
        print data.index(config.ip)
        print data.index("creator")
        print "ips correct"
    except Exception, e:
        print e
        print "ips false"


#解析graph报表页面结果
def graphget():
    datas = db.readtaskid(config.cronip)
    for i in range(0, len(datas)):
        data = "ping-"+config.cronip+"/dstIp="+config.cronip+",taskId="+str(datas[i])+",type=ping"
        task = db.readgetid(data)
        req = urllib2.Request(config.graph_ips + str(task) + "&start=-3600&cf=")
        count = 0
        try:
            response = urllib2.urlopen(req).readline()
            ss = json.loads(response)
            if len(ss["series"]) < 1:
                print "graph nodata"
                os._exit(0)
            for j in range(0, 58):
                value = ss["series"][0]["data"][j]
                if value[1] == "null":
                    count = count + 1
            if count < 58 and ss["title"] == config.description:
                print "graph response suss"
            else:
                print "graph response fail"
        except Exception, e:
            print e
            print "graph response fail"

def graphgetdns():
    datas = db.readtaskid(config.crondns)
    for i in range(0, len(datas)):
        data = "dns-"+config.crondns+"/hostname="+config.crondns+",taskId="+str(datas[i])+",type=dns"
        task = db.readgetid(data)
        req = urllib2.Request(config.graph_ips + str(task) + "&start=-3600&cf=")
        count = 0
        try:
            response = urllib2.urlopen(req).readline()
            ss = json.loads(response)
            if len(ss["series"]) < 1:
                print "graph nodata"
                os._exit(0)
            for j in range(0, 11):
                value = ss["series"][0]["data"][j]
                if value[1] == "null":
                    count = count + 1
            if count < 11 and ss["title"] == data:
                print "graph response suss"
            else:
                print "graph response fail"
        except Exception, e:
            print e
            print "graph response fail"

def graphgethttp():
    datas = db.readtaskid(config.cronhttp)
    for i in range(0, len(datas)):
        data = ""+config.httphost+"-"+str(datas[i])+"/taskId="+str(datas[i])+",type=http,url="+config.cronhttp+""
        task = db.readhttpgetid(data)
        for p in range(0, len(task)):
            req = urllib2.Request(config.graph_ips + str(task[p]) + "&start=-3600&cf=")
            print config.graph_ips + str(task[p]) + "&start=-3600&cf="
            count = 0
            try:
                response = urllib2.urlopen(req).readline()
                ss = json.loads(response)
                if len(ss["series"]) < 1:
                    print "graph nodata"
                    os._exists(0)
                for j in range(0,11):
                    value = ss["series"][0]["data"][j]
                    if value[1] == "null":
                        count = count + 1
                if count < 11 and ss["title"].index(data):
                    print "graph response suss"
                else:
                    print "graph response fail"
            except Exception, e:
                print e
                print "graph response fail"

