#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
元气工厂
###########################
# Class name: YQJ_task.py
# Version: 1.0.0
# Author: kaliOrange
# E-Mail:
# Date:2022年3月3日
###########################
# 描述：这是一个用来操作 元气酱 任务的脚本
'''

import requests, simplejson

headers_task_list = {
    'pkg': 'com.yuanqijiang.beautify.collection.pets',
    'v': '1.2.9',
    'os': 'android',
    'Host': 'server.ipolaris-tech.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.9.3'
}

headers_reward = {
    'pkg': 'com.yuanqijiang.beautify.collection.pets',
    'v': '1.2.9',
    'os': 'android',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'server.ipolaris-tech.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.9.3'
}

headers_task_complete = {
    'pkg': 'com.yuanqijiang.beautify.collection.pets',
    'v': '1.2.9',
    'os': 'android',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'server.ipolaris-tech.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.9.3'
}

headers_task_status = {
    'pkg': 'com.yuanqijiang.beautify.collection.pets',
    'v': '1.2.9',
    'os': 'android',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'server.ipolaris-tech.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.9.3'
}

url_reward = 'http://server.ipolaris-tech.com/task/reward'
url_task_list = 'http://server.ipolaris-tech.com/task/list'
url_task_status = 'http://server.ipolaris-tech.com/task/status'
url_task_complete = 'http://server.ipolaris-tech.com/task/complete'


# 激活任务
def post_task_complete(code: str, tk: str, vn: str):
    headers_task_complete['tk'] = tk
    headers_task_complete['vn'] = vn
    data_task_complete = {'taskCode': code}
    headers_task_complete['Content-Length'] = str(len(code) + 9)
    try:
        task_complete_response = requests.post(url=url_task_complete, headers=headers_task_complete,
                                               data=data_task_complete)
        reward_response_json = simplejson.loads(task_complete_response.text)
        task_complete_response.close()
        return reward_response_json
    except:
        print('状态响应数据异常')
        return False


# 执行任务
def post_reward(code: str, tk: str, vn: str):
    headers_reward['tk'] = tk
    headers_reward['vn'] = vn
    data_reward = {'taskCode': code}
    headers_reward['Content-Length'] = str(len(code) + 9)
    try:
        reward_response = requests.post(url=url_reward, headers=headers_reward, data=data_reward)
        reward_response_json = simplejson.loads(reward_response.text)
        reward_response.close()
        return reward_response_json
    except:
        print('状态响应数据异常')
        return False


# 获取任务列表
def get_task_list(tk: str, vn: str):
    headers_task_list['tk'] = tk
    headers_task_list['vn'] = vn
    try:
        task_list_requests = requests.get(url=url_task_list, headers=headers_task_list)
        task_list_json = simplejson.loads(task_list_requests.text)
        task_list_requests.close()
        return task_list_json
    except:
        print('获取任务列表失败！')
    return False


def get_task_status(code: str, tk: str, vn: str):
    headers_task_status['tk'] = tk
    headers_task_status['vn'] = vn
    data_task_status = {'taskCode': code}
    headers_task_status['Content-Length'] = str(len(code) + 9)
    try:
        task_status_response = requests.get(url=url_task_status, headers=headers_task_status, data=data_task_status)
        task_status_response_json = simplejson.loads(task_status_response.text)
        task_status_response.close()
        return task_status_response_json
    except:
        print('获取任务状态失败！')
    return False


def post_task_status(code: str, tk: str, vn: str):
    headers_task_status['tk'] = tk
    headers_task_status['vn'] = vn
    data_task_status = {'taskCode': code}
    headers_task_status['Content-Length'] = str(len(code) + 9)
    try:
        task_status_response = requests.post(url=url_task_status, headers=headers_task_status, data=data_task_status)
        task_status_response_json = simplejson.loads(task_status_response.text)
        task_status_response.close()
        return task_status_response_json
    except:
        print('获取任务状态失败！')
    return False
