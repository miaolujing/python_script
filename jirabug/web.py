#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lilian'

from flask import Flask
import search,json,gettime

app = Flask(__name__)

@app.route('/api')
def hello():
    return 'jira count'

@app.route('/api/count')
def count():
    return search.postsearch('count')

@app.route('/api/kind')
def kind():
    return search.postsearch('kind')

@app.route('/api/fixed')
def fixed():
    return search.postepic('fixed')

@app.route('/api/time')
def time():
    time = []
    dict = {}
    dict['time'] = "" + gettime.gettime('start') + "--" + gettime.gettime('end') + ""
    time.append(dict)
    return json.dumps(time)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=True)