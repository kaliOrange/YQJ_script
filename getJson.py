#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
###########################
# Class name: getJson.py
# Version: 1.1.1
# Author: kaliOrange
# E-Mail:
# Date:2022年3月3日
###########################
# 描述：这是用于获取json文件中的数据
'''
'''
cron: 59 23 31 12 *
new Env('元气酱_脚本json文件数据接口');
'''
import simplejson
def getCookies():
    with open('Json/cookie.json', 'r', encoding='utf-8') as f:
        cookies = f.read()
    return simplejson.loads(cookies)

def getTask():
    with open('Json/data.json','r',encoding='utf-8') as f:
        task = f.read()
    return simplejson.loads(task)["result"]["task"]

def getSign():
    with open('Json/data.json','r',encoding='utf-8') as f:
        sign = f.read()
    return simplejson.loads(sign)["result"]["user"]["sign"]

def getInfo():
    with open('Json/data.json','r',encoding='utf-8') as f:
        info = f.read()
    return simplejson.loads(info)["result"]["user"]["info"]

def getBubble():
    with open('Json/data.json','r',encoding='utf-8') as f:
        getBubble = f.read()
    return simplejson.loads(getBubble)["result"]["factory"]
