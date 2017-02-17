#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lilian'

import pymysql
import random
import time

dbconn = {
     'host':'10.1.53.249',
     'port':3306,
     'user':'showtestdata',
     'password':'Showtestdata123!',
     'db':'showtestdata',
     'charset':'utf8',
     'cursorclass':pymysql.cursors.DictCursor,
     }

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 +sec

class Showdata(object):

    def __init__(self):
        pass

    #更新count表，随机插入整数
    def db_count(self):
        value = random.randint(1, 99999999)
        print 'count.series:',value
        sql = "update `count` set `series` = '"+str(value)+"'"
        db = pymysql.connect(**dbconn)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except Exception, e:
            print e
            db.rollback()
        db.close()
        print "update count suss"

    #更新fcount表，随机插入浮点数，小数点后保留7位
    def db_fcount(self):
        num = random.uniform(1, 99999)
        value = round(num, 7)
        print 'fcount.series:', value
        sql = "update `fcount` set `series` = '" + str(value) + "'"
        db = pymysql.connect(**dbconn)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
        except Exception, e:
            print e
            db.rollback()
        db.close()
        print "update fcount suss"

    #先清空pie，再插入六条数据
    def db_pie(self):
        delsql = "delete from pie"
        db = pymysql.connect(**dbconn)
        cursor = db.cursor()
        try:
            cursor.execute(delsql)
            db.commit()
        except Exception, e:
            print e
            db.rollback()
        list = []
        chartsname = [u"羊毛", u"聚酯纤维", u"亚麻", u"羊绒", u"锦纶", u"腈纶"]
        addsql = "insert into pie(chartsName,chartsNum) VALUES(%s,%s)"
        for i in range(0,len(chartsname)):
            num = random.uniform(10, 100000)
            chartsnum = round(num, 3)
            data = (chartsname[i],chartsnum)
            list.append(data)
        print 'pie value:',list
        try:
            cursor.executemany(addsql,list)
            db.commit()
        except Exception, e:
            print e
            db.rollback()
        db.close()
        print "insert pie suss"

    #先清空persent，再插入五条数据，值总和为100
    def db_persent(self):
        delsql = "delete from persent"
        db = pymysql.connect(**dbconn)
        cursor = db.cursor()
        try:
            cursor.execute(delsql)
            db.commit()
        except Exception, e:
            print e
            db.rollback()
        addsql = "insert into persent(`name`,`value`) VALUES(%s,%s)"
        list = []
        names = [100,101,200,201,202,203,206,300,301,302,400,401,402,403,404,500,502,503,504,505]
        values = []
        a = random.randint(0, 99)
        values.append(a)
        b = round(random.uniform(0, 100-a), 2)
        values.append(b)
        c = random.randint(0, round((100-a-b), 0))
        values.append(c)
        d = round(random.uniform(0, 100-a-b-c), 2)
        values.append(d)
        e = round(100-a-b-c-d, 2)
        values.append(e)
        for i in range(0,len(values)):
            j = random.randint(0,len(names)-1)
            data = (names[j],values[i])
            names.remove(names[j])
            list.append(data)
        print 'persent value:',list
        try:
            cursor.executemany(addsql,list)
            db.commit()
        except Exception, e:
            print e
            db.rollback()
        db.close()
        print "insert persent suss"

    #先创建临时表，再对map种warncount和linkcount批量更新，整数
    def db_map(self):
        db = pymysql.connect(**dbconn)
        cursor = db.cursor()
        createsql = "create temporary table `tmp`(`id` int(19) not null auto_increment,`warnCount` double DEFAULT NULL,`linkCount` double DEFAULT NULL,primary key (id))engine=innodb default charset=utf8"
        dropsql = "drop temporary table if exists `tmp`"
        try:
            cursor.execute(dropsql)
            cursor.execute(createsql)
        except Exception, e:
            print e
        addsql = "insert into `tmp`(`warnCount`,`linkCount`) VALUES(%s,%s)"
        replacesql = "update `map`,`tmp` set `map`.`warnCount`=`tmp`.`warnCount`,`map`.`linkCount`=`tmp`.`linkCount` where `map`.id=`tmp`.id"
        list = []
        for i in range(0,42):
            warncount = random.randint(1,99999)
            linkcount = random.randint(1,100000)
            data = (warncount,linkcount)
            list.append(data)
        print 'replace value:',list
        try:
            cursor.executemany(addsql,list)
            cursor.execute(replacesql)
            db.commit()
        except Exception, e:
            print e
            db.rollback()
        db.close()
        print "replace map succ"

    #更新ram，整数，不超过200
    def db_ram(self):
        db = pymysql.connect(**dbconn)
        cusor = db.cursor()
        value = random.randint(1, 200)
        print 'ram.series:', value
        sql = "update `ram` set `series` = '" + str(value) + "'"
        try:
            cusor.execute(sql)
            db.commit()
        except Exception, e:
            print e
            db.rollback()
        db.close()
        print "update ram suss"

    #更新fram，浮点数，不超过200
    def db_fram(self):
        db = pymysql.connect(**dbconn)
        cusor = db.cursor()
        value = round(random.uniform(0, 200), 4)
        print 'fram.series:', value
        sql = "update `fram` set `series` = '" + str(value) + "'"
        try:
            cusor.execute(sql)
            db.commit()
        except Exception, e:
            print e
            db.rollback()
        db.close()
        print "update fram suss"

if __name__ == "__main__":
    second = sleeptime(0,0,15)
    while True:
        showdata = Showdata()
        showdata.db_count()
        showdata.db_fcount()
        showdata.db_pie()
        showdata.db_persent()
        showdata.db_map()
        showdata.db_ram()
        showdata.db_fram()
        time.sleep(second)
