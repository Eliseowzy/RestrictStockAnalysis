# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@file: excel_config.py
@time: 9/29/2021
@version: 1.0
"""
import utils.excel_config as excel_config
import utils.stock_calculator as stock_calculator

stocks = excel_config.get_list_by_column(file_name='../data/restrict_stock_detail_20210909.csv', column_name='代码', encoding='gb18030')
# print(stocks)
stock_change_ratio_list = {}

for stock in stocks:
    tmp_ratio = stock_calculator.get_stock_change_ratio(stock_code=stock, start_date="20210909", end_date="20210929")

    if tmp_ratio:
        # print("{}\t{}".format(stock, tmp_ratio))
        print(tmp_ratio)
