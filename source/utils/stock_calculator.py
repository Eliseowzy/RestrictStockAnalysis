# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@file: stock_calculator.py
@time: 9/29/2021
@version: 1.0
"""

import datetime

from source.utils import data_extractor
from source.utils import data_preprocessor


def calculate_basic_eps():
    stocks = data_preprocessor.get_list_by_column(file_path='../data/聚类数据集.xlsx', column_name='代码')
    for stock in stocks:
        try:
            tmp_basic_eps = data_extractor.get_company_latest_basic_eps(stock)
            print(tmp_basic_eps)
        except IndexError:
            print("")


def calculate_return_rate(day_slot=90):
    stocks = data_preprocessor.get_list_by_column(file_path='../../data/聚类数据集.xlsx', column_name='代码')

    release_dates = data_preprocessor.get_list_by_column(file_path='../../data/聚类数据集.xlsx', column_name='解禁日期')
    stock_change_ratio_list = {}

    for i in range(len(stocks)):
        start_date = datetime.datetime.date(release_dates[i])
        delta = datetime.timedelta(days=day_slot)
        end_date = start_date + delta

        start_date = datetime.datetime.strftime(start_date, "%Y%m%d")
        end_date = datetime.datetime.strftime(end_date, "%Y%m%d")
        tmp_ratio = data_extractor.get_stock_change_ratio(stock_code=stocks[i], start_date=start_date,
                                                          end_date=end_date)

        if tmp_ratio:
            print("{}\t{}".format(stocks[i], tmp_ratio))
        else:
            print('{}\t'.format(stocks[i]))
