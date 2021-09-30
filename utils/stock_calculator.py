# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@file: stock_calculator.py
@time: 9/29/2021
@version: 1.0
"""
import pandas as pd
import tushare as ts


def get_stock_change_detail_info(stock_code='301013.SZ', start_date='20210920', end_date='20210929'):
    """Get stock change price detail information.

    Returns:
        pandas.DataFrame 'stock_change_detail_info': A stock price change detail info.
    """
    pd.set_option('display.max_columns', None)
    pro = ts.pro_api()
    stock_change_detail_info = pro.query('daily', ts_code=stock_code, start_date=start_date, end_date=end_date)
    stock_change_detail_info = stock_change_detail_info.sort_values(by='trade_date', ascending=True)
    return stock_change_detail_info


def get_stock_change_ratio(stock_code='301013.SZ', start_date='20210920', end_date='20210929'):
    """Get stock change price ratio.

    Returns:
        pandas.DataFrame 'stock_change_detail_info': A stock price change detail info.
    """
    stock_change_detail_info = get_stock_change_detail_info(stock_code=stock_code, start_date=start_date,
                                                            end_date=end_date)
    size = len(stock_change_detail_info['close'])
    # print(stock_change_detail_info)
    if size != 0:
        stock_change = stock_change_detail_info['close'][size - 1] - stock_change_detail_info['close'][0]
        stock_change_ratio = stock_change / stock_change_detail_info['close'][0]
        # print(stock_change_ratio)
        # print(stock_code)
        return stock_change_ratio

    #


# print(get_stock_change_info(stock_code='301013.SZ', start_date='20210920', end_date='20210929'))
get_stock_change_ratio()
