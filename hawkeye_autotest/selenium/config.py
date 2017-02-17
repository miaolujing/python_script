#!/usr/bin/env python
# -*- coding: utf-8 -*-

#fe登陆地址及用户名密码
baseurl = "http://172.30.37.120:1234"
user = "root"
passwd = "123456"
#测试ip管理页面新增ip
ip = "125.118.85.77"
#新增定时任务地址
host = "172.30.37.120"
port = "5050"
#数据库地址
mysqlhost = "172.30.37.148"
mysqluser = "root"
mysqlpw = "123456"
mysqlssid = "hportal"
dashssid = "dashboard"
#定时任务新增信息
cronip = "115.200.245.116"
description = u"115.200.245.116(电信-浙江省杭州市-)"
cronhttp = "http://58.216.6.25/newsapp_bt/0/143507856/640"
httphost = "inews.gtimg.com"
crondns = "www.baidu.com"
cronhost1 = "fewrw.novalocal;172.30.41.23"
cronhost2 = "shata-shc-vmci-person-tongwei05.novalocal;172.30.41.24"
#监控图管理新建
monitorhost = "172.30.37.120"
monitorport = "8081"
#调用使sig生效
loginurl = "http://172.30.37.120:1234/auth/login"
#监控图管理二级菜单name
secondmenu = "mljtests"
#监控图管理节点host/监控图报表名称
dashhost = "fewrw.novalocal\r\nshata-shc-vmci-person-tongwei05.novalocal"
dashhost1 = "fewrw.novalocal"
dashhost2 = "shata-shc-vmci-person-tongwei05.novalocal"
pingname = "mljping"
dnsname = "mljdns"
httpname = "mljhttp"
#screen页面图表get地址
graph_ips = "http://172.30.37.120:8081/chart/h?id="
#删除定时任务get地址
crondel = "http://172.30.37.120:5050/tasks/delete/"

#ip管理搜索页面get地址
hportal_ips = "http://172.30.37.120:5050/ips?q="
