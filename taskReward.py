#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
元气工厂
###########################
# Class name: taskReward.py
# Version: 1.1.1
# Author: kaliOrange
# E-Mail:
# Date:2022年3月3日
###########################
# 描述：这是 元气酱 每日任务完成脚本
'''
'''
cron: 3 0 * * *	
new Env('元气酱_每日任务');
'''
import simplejson,time
import getJson,task,getInfo

# 点击完成任务
def run(tk: str, vn: str):
    # 打印当前用户元气总数
    print('当前用户元气总数：' + str(getInfo.get(tk=tk, vn=vn)['result']['coin']))
    # 获取每日任务列表JSON
    task_list_json = task.get_task_list(tk=tk, vn=vn)
    if task_list_json == False:
        print('获取任务列表失败！')
        return False

    # 遍历每日任务列表
    for task_json in task_list_json['result']:
        print('任务名称：'+ task_json['name']+'\t状态：',end='')
        # 判断任务状态是否是完成，是：else，否：执行
        if task_json['status']!= "received":
            print('未完成')
            print('执行任务中：',end='')
            # 判断任务是否是uncompleted未激活状态
            if task_json['status'] == "uncompleted":
                # 激活任务
                task.post_task_complete(code=task_json['code'],tk=tk, vn=vn)

            # 遍历任务,如果任务未完成次数小于2：执行一次。否则else，遍历任务
            if (task_json['total'] - task_json['count'])<2:
                task.post_reward(tk=tk, vn=vn, code=task_json['code'])
            else:
                # 遍历任务总次数total-任务已做count次数
                for count in range(task_json['total'] - task_json['count']):
                    task.post_reward(tk=tk, vn=vn, code=task_json['code'])
                    time.sleep(60)
            print('已成功执行脚本...')
        else:
            print('已完成')

    print('-'*10)
    print('正在检查任务状态...')
    task_list_json = task.get_task_list(tk=tk, vn=vn)
    for task_json in task_list_json['result']:
        print('任务名称：' + task_json['name'] + '\t状态：', end='')
        print('已完成' if task_json['status'] == 'received' else '未完成')
    # 打印当前用户元气总数
    print('当前用户元气总数：' + str(getInfo.get(tk=tk, vn=vn)['result']['coin']))

# 获取YQJ_cookie.json文本数据
cookies = getJson.getCookies()

# 转换数据为json数据并遍历cookies
for cookie in cookies['cookies']:
    # 打印用户名
    print('-' * 20)
    print('当前用户：' + cookie['name'])
    # 批量执行
    run(cookie['tk'], cookie['vn'])
