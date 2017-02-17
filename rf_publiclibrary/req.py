#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lilian'

import requests
import login
import publiclibrary
import json

public = publiclibrary.PublicLibrary()

class Req(object):

    def __init__(self):
        pass

    def nreq(self,url,method,data=None):
        headers = {'Content-Type': "application/json",'Accept': "application/json",'cookie': ""+login.cook_value+""}
        print headers
        if data:
            data = public.eval_dict(data)
        try:
            if method == "post":
                if isinstance(data,dict):
                    data = json.dumps(data)
                results = requests.post(url,data=data,headers=headers,verify=False)
            elif method == "get":
                results = requests.get(url,params=data,headers=headers,verify=False)
            elif method == 'delete':
                results = requests.delete(url, headers=headers, verify=False)
            elif method == 'put':
                if isinstance(data, dict):
                    data = json.dumps(data)
                results = requests.put(url, data=data, headers=headers, verify=False)
            return results
        except requests.ConnectionError as e:
            print e

    def nget_errcode(self,url,method,data=None):
        headers = {'Content-Type': "application/json", 'Accept': "application/json",
                   'cookie': "" + login.cook_value + ""}
        print headers
        if data:
            data = public.eval_dict(data)
        try:
            if method == "post":
                if isinstance(data, dict):
                    data = json.dumps(data)
                results = requests.post(url, data=data, headers=headers, verify=False)
            elif method == "get":
                results = requests.get(url, params=data, headers=headers, verify=False)
            elif method == 'delete':
                results = requests.delete(url, headers=headers, verify=False)
            elif method == 'put':
                if isinstance(data, dict):
                    data = json.dumps(data)
                results = requests.put(url, data=data, headers=headers, verify=False)
            return json.loads(results.content)['errCode']
        except requests.ConnectionError as e:
            print e

if __name__ == '__main__':
    pass