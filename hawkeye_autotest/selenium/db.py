#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config, re, MySQLdb, MySQLdb.cursors

#数据库查询数据--给screen建counter使用
def readtaskid(des):
    db = MySQLdb.connect(config.mysqlhost,config.mysqluser,config.mysqlpw,config.mysqlssid)
    cursor = db.cursor()
    sql = "select taskid from scheduletask where description like '%"+des+"%' and status = '0'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        data = []
        for i in range(0, len(results)):
            data.append(results[i][0])
        return data
    except Exception, e:
        print e
    db.close()

def readip(des):
    db = MySQLdb.connect(config.mysqlhost,config.mysqluser,config.mysqlpw,config.mysqlssid)
    cursor = db.cursor()
    sql = "select id from ip where ip_name = '"+des+"'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return len(results)
    except Exception, e:
        print e
    db.close()

#数据库查询监控任务二级菜单id
def readid():
    db = MySQLdb.connect(config.mysqlhost,config.mysqluser,config.mysqlpw,config.dashssid)
    cursor = db.cursor()
    sql = "select id from dashboard_screen where name = '"+config.secondmenu+"'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results[0][0]
    except Exception, e:
        print e
    db.close()

#判断监控报表新增
def readmonitor(des):
    db = MySQLdb.connect(config.mysqlhost,config.mysqluser,config.mysqlpw,config.dashssid)
    cusor = db.cursor()
    sql = "select title from dashboard_graph where counters = '"+des+"'"
    try:
        cusor.execute(sql)
        results = cusor.fetchall()
        return results[0][0]
    except Exception, e:
        print e
        return False
    db.close()

#获取报表get地址的id
def readgetid(des):
    db = MySQLdb.connect(config.mysqlhost,config.mysqluser,config.mysqlpw,config.dashssid)
    cusor = db.cursor()
    sql = "select id from tmp_graph where counters = '"+des+"'"
    try:
        cusor.execute(sql)
        results = cusor.fetchall()
        return results[0][0]
    except Exception, e:
        print e
        return False
    db.close()

def readhttpgetid(des):
    db = MySQLdb.connect(config.mysqlhost,config.mysqluser,config.mysqlpw,config.dashssid)
    cusor = db.cursor()
    sql = "select id from tmp_graph where counters like '%"+des+"'"
    try:
        cusor.execute(sql)
        results = cusor.fetchall()
        data = []
        for i in range(0, len(results)):
            data.append(results[i][0])
        return data
    except Exception, e:
        print e
        return False
    db.close()

#获取定时任务id
def readcronid(des):
    db = MySQLdb.connect(config.mysqlhost,config.mysqluser,config.mysqlpw,config.mysqlssid)
    cursor = db.cursor()
    sql = "select id from scheduletask where description like '%"+des+"%' and status = '0'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        data = []
        for i in range(0, len(results)):
            data.append(results[i][0])
        return data
    except Exception, e:
        print e
    db.close()
















