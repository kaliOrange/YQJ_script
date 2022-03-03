#!/usr/bin/python
#-*- coding:UTF-8 -*-
'''
元气工厂
###########################
# Class name: YQJ_getInfo.py
# Version: 1.0.0
# Author: kaliOrange
# E-Mail:
# Date:2022年2月26日
###########################
# 描述：这是用与获取元气酱APP元气工厂的元气
# 版本更新： 1.修改getBubbleNumber()函数：getBubble(),返回值为json
'''


import requests,simplejson

# 获取用户info数据请求头
getInfo_headers = {
'pkg': 'com.yuanqijiang.beautify.collection.pets',
'v': '1.2.9',
'os': 'android',
'Host': 'server.ipolaris-tech.com',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'User-Agent': 'okhttp/4.9.3'
}

# 获取user数据URL
url_info = 'http://server.ipolaris-tech.com/user/info'

# 设置用户tk和vn
def default_headers(tk:str,vn:str):
    getInfo_headers['tk']=tk
    getInfo_headers['vn']=vn

def getInfo(tk:str,vn:str):
    default_headers(tk,vn)
    try:
        # 获取用户信息
        info_response = requests.get(url=url_info, headers=getInfo_headers)
        # 把info_response转为json数据
        info_json = simplejson.loads(info_response.text)
        # 释放info_response
        info_response.close()
        # 判断info_json状态
        if info_json['ret'] == 200 :
            return info_json
        else:
            print('状态码异常！')
    except:
        print('获取用户信息失败！')
        info_response.close()
    return False
    # return requests.get(url=url_info,headers=getInfo_headers).text

def get(tk:str,vn:str):
    return getInfo(tk=tk, vn=vn)