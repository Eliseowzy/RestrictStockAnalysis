# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@function: unit test for each module
@file: unit_test.py
@time: 14/10/2021
@version: 1.0
"""
# "http://10.23.163.236/23/pc.html?url_id=14737290?switch_url=http://10.23.128.128/login.html&ap_mac=00:d7:8f:01:4b:d0&client_mac=04:ed:33:dd:8f:06&wlan=Citics-public&redirect=www.msftconnecttest.com/redirect"
s = """
工业
信息技术
工业
信息技术
医疗保健
信息技术
材料
医疗保健
医疗保健
材料
材料
信息技术
工业
工业
能源
信息技术
工业
日常消费
工业
工业
医疗保健
信息技术
日常消费
能源
可选消费
信息技术
工业
工业
工业
材料
信息技术
工业
公用事业
医疗保健
可选消费
工业
医疗保健
日常消费
工业
日常消费
工业
电信服务
材料
工业
工业
日常消费
日常消费
工业
工业
工业
信息技术
信息技术
可选消费
工业
医疗保健
信息技术
医疗保健
能源
信息技术
信息技术
工业
医疗保健
可选消费
工业
材料
信息技术
日常消费
工业
工业
日常消费
材料
可选消费
材料
工业
工业
材料
信息技术
工业
工业
材料
工业
材料
信息技术
可选消费
材料
信息技术
工业
工业
工业
医疗保健
信息技术
日常消费
材料
金融
工业
"""
ls = s.split()
ls = set(ls)
print(ls)
