#!/usr/bin/python
#-*- coding:UTF-8 -*-
'''
元气工厂
###########################
# Class name: getInfo.py
# Version: 1.0.0
# Author: kaliOrange
# E-Mail:
# Date:2022年2月26日
###########################
# 描述：这是用与获取元气酱APP 用户信息接口
'''
'''
cron: 59 23 31 12 *
new Env('元气酱_用户信息脚本接口');
'''

import requests,simplejson,getJson

info_json = getJson.getInfo()
# 获取用户info数据请求头
getInfo_headers = info_json['headers']['info']

# 获取user数据URL
url_info = info_json['url']['info']

# 获取用户信息
def getInfo(tk:str,vn:str):
    getInfo_headers['tk']=tk
    getInfo_headers['vn']=vn
    try:
        # 获取用户信息
        info_response = requests.get(url=url_info, headers=getInfo_headers)
        # 把info_response转为json数据
        info_json = simplejson.loads(info_response.text)
        # 释放info_response
        info_response.close()
        return info_json
    except:
        print('获取用户信息失败！')
    return False

def get(tk:str,vn:str):
    return getInfo(tk=tk, vn=vn)