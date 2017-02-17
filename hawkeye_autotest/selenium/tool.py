#!/usr/bin/env python
# -*- coding: utf-8 -*-

#解析页面结果
import urllib2, config, re
from bs4 import BeautifulSoup

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