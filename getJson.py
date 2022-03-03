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
new Env('元气酱_脚本json文件数据接口');
'''
import simplejson
def getCookies():
    with open('Json/cookie.json', 'r', encoding='utf-8') as f:
        cookies = f.read()
    return simplejson.loads(cookies)

def getTask():
    with open('Json/task.json','r',encoding='utf-8') as f:
        task = f.read()
    return simplejson.loads(task)

def getSign():
    with open('Json/sign.json','r',encoding='utf-8') as f:
        sign = f.read()
    return simplejson.loads(sign)

def getInfo():
    with open('Json/info.json','r',encoding='utf-8') as f:
        info = f.read()
    return simplejson.loads(info)

def getBubble():
    with open('Json/bubble.json','r',encoding='utf-8') as f:
        bubble = f.read()
    return simplejson.loads(bubble)
