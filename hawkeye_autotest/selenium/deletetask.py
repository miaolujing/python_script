#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, config, urllib2, db, addtask

def crondel(des):
    datas = db.readcronid(des)
    for i in range(0, len(datas)):
        req = urllib2.Request(config.crondel + str(datas[i]))
        req.add_header('Cookie','sig='+addtask.getsig()+'')
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError as e:
            if hasattr(e, 'code'):
                print 'Error code:',e.code
            elif hasattr(e, 'reason'):
                print 'Reason:',e.reason
