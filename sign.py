#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
元气工厂
###########################
# Class name: sign.py
# Version: 1.1.1
# Author: kaliOrange
# E-Mail:
# Date:2022年3月3日
###########################
# 描述：这是 元气酱 每日签到完成脚本
'''
'''
cron: 53 0 * * *	
new Env('元气酱_每日签到');
'''
import requests, simplejson
import getInfo,task,getJson

sign_json = getJson.getSign()

# 设置用户tk和vn
def default_headers(tk: str, vn: str):
    headers_sign['tk'] = tk
    headers_sign['vn'] = vn
    headers_sign_status['tk'] = tk
    headers_sign_status['vn'] = vn


headers_sign = sign_json['v1']['headers']

headers_sign_status = sign_json['record']["v1"]['headers']

url_sign = sign_json['v1']['url']
url_sign_status = sign_json['record']["v1"]['url']


def run(tk: str, vn: str):
    # 打印当前用户元气总数
    print('当前用户元气总数：' + str(getInfo.get(tk=tk, vn=vn)['result']['coin']))
    # 初始化cookie
    default_headers(tk=tk, vn=vn)
    # 获取签到状态
    print('签到状态：', end='')
    sign_status_json = get_sign_status(tk=tk, vn=vn)
    if sign_status_json != False:
        # 判断：未签到执行签到，已签到则跳过
        if sign_status_json['result']['todaySign'] == True:
            print('已签到')
        else:
            print('未签到')
            print('正在执行签到...\t', end='')
            try:
                # 执行签到任务
                sing_response_json = requestSing(tk=tk, vn=vn)
                # 再次获取签到状态

                if get_sign_status(tk=tk, vn=vn)['result']['todaySign'] == True:
                    print('签到成功', end='')
                    print('获取' + str(sing_response_json['result']['coin']) + '元气')
                else:
                    print('签到失败')
            except:
                print('请求失败，未知错误')

    # 获取激励任务状态
    print('"视频激励翻倍奖励"任务状态：', end='')
    task_status_json = task.post_task_status(tk=tk, vn=vn, code='x_task_002')
    if task_status_json != False:
        # 判断：未签到执行签到，已签到则跳过
        if task_status_json['result']['status'] == 'received':
            print('已完成')
        else:
            print('未完成')
            print('正在执行任务...\t', end='')
            if task_status_json['result']['status'] == 'uncompleted':
                task.post_task_complete(tk=tk, vn=vn, code='x_task_002')
            if task.post_task_status(tk=tk, vn=vn, code='x_task_002')['result']['status'] == 'completed':
                print('获取' + str(task.post_reward(tk=tk, vn=vn, code='x_task_002')['result']['reward']['coin']) + '元气\t',
                      end='')
            if task.post_task_status(tk=tk, vn=vn, code='x_task_002')['result']['status'] == 'received':
                print('已完成')
    # 打印当前用户元气总数
    print('当前用户元气总数：' + str(getInfo.get(tk=tk, vn=vn)['result']['coin']))

def get_sign_status(tk: str, vn: str):
    headers_sign_status['tk'] = tk
    headers_sign_status['vn'] = vn
    try:
        sign_status_response = requests.get(url=url_sign_status, headers=headers_sign_status)
        sign_status_response_json = simplejson.loads(sign_status_response.text)
        return sign_status_response_json
    except:
        print('未知错误。')
    return False


def requestSing(tk: str, vn: str):
    headers_sign['tk'] = tk
    headers_sign['vn'] = vn
    try:
        sing_response = requests.get(url=url_sign, headers=headers_sign)

        sing_response_json = simplejson.loads(sing_response.text)
        if sing_response_json['ret'] == 9017:
            print('响应码9022，今天已完成签到！')
            return False

        if sing_response_json['ret'] != 200:
            print('签到失败，json状态码异常.')
            return False

        print('签到成功')
        return sing_response_json
    except:
        print('签到失败，未知的脚本异常.')
    return False


# 获取YQJ_cookie.json文本数据
try:
    with open('Json/cookie.json', 'r', encoding='utf-8') as f:
        cookies = f.read()
except:
    print('获取COOKIE失败！请检查YQJ_cookie.json文件是否存在.')

for cookie in simplejson.loads(cookies)['cookies']:
    # 打印用户名
    print('-' * 20)
    print('当前用户：' + cookie['name'])
    # 批量执行
    run(cookie['tk'], cookie['vn'])
