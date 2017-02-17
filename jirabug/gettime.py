#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lilian'

from datetime import datetime,timedelta

def gettime(type):
    ISOTIMEFORMAT = '%Y-%m-%d'
    today = datetime.now()
    last = today + timedelta(days=-37)
    if type == 'start':
        return last.strftime(ISOTIMEFORMAT)
    if type == 'end':
        return today.strftime(ISOTIMEFORMAT)
