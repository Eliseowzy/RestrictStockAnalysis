# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@function: unit test for each module
@file: unit_test.py
@time: 14/10/2021
@version: 1.0
"""


class People:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # res = "对象的名字是{}".format(self.name)
        # return res
        return self.name


a = People("abc")
print(a)
