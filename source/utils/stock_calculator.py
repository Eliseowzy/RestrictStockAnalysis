# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@file: stock_calculator.py
@time: 9/29/2021
@version: 1.0
"""

import datetime

from source.utils import data_preprocessor
from source.utils import stock_index_extracter


def calculate_basic_eps():
    stocks = data_preprocessor.get_list_by_column(file_path='../data/聚类数据集.xlsx', column_name='代码')
    for stock in stocks:
        try:
            tmp_basic_eps = stock_index_extracter.get_company_latest_basic_eps(stock)
            print(tmp_basic_eps)
        except IndexError:
            print("")


def calculate_return_rate(day_slot=90):
    stocks = data_preprocessor.get_list_by_column(file_path='../../data/聚类数据集.xlsx', column_name='代码')

    release_dates = data_preprocessor.get_list_by_column(file_path='../../data/聚类数据集.xlsx', column_name='解禁日期')
    # print(stocks)
    stock_change_ratio_list = {}

    for i in range(len(stocks)):
        start_date = datetime.datetime.date(release_dates[i])
        delta = datetime.timedelta(days=day_slot)
        end_date = start_date + delta

        start_date = datetime.datetime.strftime(start_date, "%Y%m%d")
        end_date = datetime.datetime.strftime(end_date, "%Y%m%d")
        tmp_ratio = stock_index_extracter.get_stock_change_ratio(stock_code=stocks[i], start_date=start_date,
                                                                 end_date=end_date)
        # print(stocks[i])
        if tmp_ratio:
            print("{}\t{}".format(stocks[i], tmp_ratio))
            # print(tmp_ratio)
            # print(stocks[i])
        else:
            print('{}\t'.format(stocks[i]))


if __name__ == "__main__":
    calculate_return_rate()
