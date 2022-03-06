#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
元气工厂
###########################
# Class name: getBubble2.py
# Version: 1.1.0
# Author: kaliOrange
# E-Mail:
# Date:2022年2月26日
###########################
# 描述：这是用与获取元气酱APP元气工厂的元气
# 版本更新：
'''
'''
cron: */40 */2 * * *
new Env('元气酱_元气工厂_02');
'''
import requests, simplejson
import getJson, getInfo

bubble_json = getJson.getBubble()


# 设置用户tk和vn
def default(tk: str, vn: str):
    headers_status['tk'] = tk
    headers_status['vn'] = vn
    headers_getBubble['tk'] = tk
    headers_getBubble['vn'] = vn
    headers_upgrade['tk'] = tk
    headers_upgrade['vn'] = vn


# status用于获取元气工厂状态的get请求头
headers_status = bubble_json['status']['headers']

# getBubble用于获取元气工厂元气的post请求头
headers_getBubble = bubble_json['getBubble']['headers']
# getBubbleData用于获取元气工厂元气的post请求数据
getBubbleData = {'type': 'all'}

headers_upgrade = bubble_json['upgrade']['headers']

# 获取元气工厂状态URL
url_getStatus = bubble_json['status']['url']

# 获取元气工厂元气URL
url_getBubble = bubble_json['getBubble']['url']

# 升级元气工厂URL
url_upgrade = bubble_json['upgrade']['url']


def main():
    # 获取YQJ_cookie.json文本数据
    cookies = getJson.getCookies()
    # 转换数据为json数据并遍历cookies
    for cookie in cookies['cookies']:
        # 批量执行
        getBubble(cookie['tk'], cookie['vn'])


# run
def getBubble(tk: str, vn: str):
    default(tk=tk, vn=vn)
    print('-' * 20)
    # 打印当前用户名
    print('当前用户：' + str(getInfo.get(tk=tk, vn=vn)['result']['nickName']))

    # 获取元气工厂元气状态
    bubbleStatus = getBubbleStatus()
    if bubbleStatus == False:
        print('获取元气工厂状态失败，跳过此用户！')
        return False

    # 获取升级工厂需求元气数
    price = bubbleStatus['result']['nextLevelFactory']['price']
    # 打印当前用户元气总数
    print('当前用户元气总数：' + str(getInfo.get(tk=tk, vn=vn)['result']['coin']))
    # 判断是否可升级工厂
    print('当前工厂等级：' + str(bubbleStatus['result']['factory']['level']))
    if price <= getInfo.get(tk=tk, vn=vn)['result']['coin']:
        # 升级元气工厂
        print('已达到升级要求，开始升级工厂等级。     ', end='')
        upgrade()
    else:
        print('升级需要 ' + str(price) + ' 元气，未达到升级条件，跳过升级。')
    # 获取元气工厂元气数量
    bubble_number = bubbleStatus['result']['bubble']
    print('元气工厂元气数：' + str(bubble_number))
    # 判断当前元气是否大于等于10：是-》获取元气 | 否-》 不获取
    if bubble_number >= 5:
        # 获取元气工厂元气
        Bubble_response = requests.post(url=url_getBubble, headers=headers_getBubble, data=getBubbleData)
        # 判断响应状态码
        if Bubble_response.status_code != 200:
            print('获取元气工厂元气响应异常。')
            return False
    else:
        print('未达到收获条件。')
        return False
    print('当前用户元气总数：' + str(getInfo.getInfo(tk=tk, vn=vn)['result']['coin']))


# 获取元气工厂元气状态
def getBubbleStatus():
    # 获取元气工厂状态
    status_response = requests.get(url=url_getStatus, headers=headers_status)

    # 判断响应码，不为 200 退出
    if status_response.status_code != 200:
        print('态码异常,响应码为： ' + status_response.status_code)
        status_response.close()
        return False
    # 把响应数据转为json
    status_json = simplejson.loads(status_response.text)
    # 判断json状态码 和 json键值
    if 'ret' not in status_json or status_json['ret'] != 200:
        print('获取元气工厂状态响应数据异常')
        status_response.close()
        return False
    # 返当前回元气工厂元气数量
    status_response.close()
    return status_json


def upgrade():
    upgrade_response = requests.post(url=url_upgrade, headers=headers_upgrade)
    try:
        upgrade_json = simplejson.loads(upgrade_response.text)
        if upgrade_json['ret'] == 200:
            print('升级成功！')
            upgrade_response.close()
            return True
    except:
        print('升级失败！')
    upgrade_response.close()
    return False


if __name__ == '__main__':
    main()
