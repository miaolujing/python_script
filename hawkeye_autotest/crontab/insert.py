#!/usr/bin/env python
# coding=utf8

import MySQLdb, config

db = MySQLdb.connect(config.mysqlhost,config.mysqluser,config.mysqlpw,config.mysqlssid)

class ReadFile:
    def readLines(self):
        f = open("/Users/miulujing/PycharmProjects/hawkeye_autotest/crontab/data.txt","r")
        list = []
        cursor = db.cursor()
        sql = "INSERT INTO scheduletask(hostname,ip,taskid,timeout,type,description,status)\
                   VALUES(%s,%s,%s,%s,%s,%s,%s)"
        for line in f:
            strs = line.split(" ")
            print len(strs)
            if len(strs) != 7:
                continue
            data = (strs[0],strs[1],strs[2],strs[3],strs[4],strs[5],strs[6].replace("\n",""))
            list.append(data)
        try:
            cursor.executemany(sql,list)
            db.commit()
        except Exception, e:
            print e
            db.rollback()
        db.close()
        f.close()
        print "insert suss"

if __name__ == "__main__":
    readFile = ReadFile()
    readFile.readLines()



















