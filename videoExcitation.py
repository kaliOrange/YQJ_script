#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
###########################
# Class name: videoExcitation.py
# Version: 1.0.0
# Author: kaliOrange
# E-Mail:
# Date:2022年3月3日
###########################
# 描述：这是一个用来操作 元气酱 每日视频激励任务的脚本
'''
'''
cron: 59 1 * * *
new Env('元气酱_每日视频激励任务');
'''


import simplejson,requests
import getJson,task,getInfo,time



def run(tk: str, vn: str):
    try:
        # 打印当前用户元气总数
        print('当前用户元气总数：' + str(getInfo.get(tk=tk, vn=vn)['result']['coin']))
    except:
        print("错误：cookie失效或网络异常！")
        return False
    codes = ["x_task_001","x_task_002"]
    for code in codes:
        response_json = task.post_task_status(tk=tk,vn=vn,code=code)
        if response_json:
            try:
                print('任务名称：'+ response_json["result"]['name']+'\t状态：',end='')
                if response_json["result"]['status'] != "received":
                    print('未完成')
                    print('执行任务中：', end='')
                    # 判断任务是否是uncompleted未激活状态
                    if response_json["result"]['status'] == "uncompleted":
                        # 激活任务
                        task.post_task_complete(code=response_json["result"]['code'], tk=tk, vn=vn)
                        # 遍历任务,如果任务未完成次数小于2：执行一次。否则else，遍历任务
                        if (response_json["result"]['total'] - response_json["result"]['count']) < 2:
                            task.post_reward(tk=tk, vn=vn, code=response_json["result"]['code'])
                        else:
                            # 遍历任务总次数total-任务已做count次数
                            for count in range(response_json["result"]['total'] - response_json["result"]['count']):
                                task.post_reward(tk=tk, vn=vn, code=response_json["result"]['code'])
                                time.sleep(60)
                        print('已成功执行脚本...')
                else:
                    print('已完成')
            except:
                print("response_json数据异常")

    print('-' * 10)
    print('正在检查任务状态...')

    for code in codes:
        response_json = task.post_task_status(tk=tk, vn=vn, code=code)
        if response_json:
            try:
                print('任务名称：' + response_json["result"]['name'] + '\t状态：', end='')
                print('已完成' if response_json["result"]['status'] == 'received' else '未完成')
            except:
                print("response_json数据异常")

    print('当前用户元气总数：' + str(getInfo.get(tk=tk, vn=vn)['result']['coin']))



# 获取YQJ_cookie.json文本数据
cookies = getJson.getCookies()

# 转换数据为json数据并遍历cookies
for cookie in cookies['cookies']:
    # 打印用户名
    print('-' * 20)
    print('当前用户：' + cookie['name'])
    # 批量执行
    run(tk=cookie['tk'], vn=cookie['vn'])
