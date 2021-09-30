# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@file: excel_config.py
@time: 9/29/2021
@version: 1.0
"""
import pandas as pd

pd.set_option('display.max_columns', None)


def get_list_by_column(file_name='./data/限售股解禁公司明细-20210909.xlsx', column_name='代码', encoding='gb18030'):
    """Get stock name list from a table.

    Returns:
        list 'code': A stock code list.
    """
    df = pd.read_csv(file_name, encoding=encoding)
    stock_code_list = []
    for stock in df[column_name]:
        stock_code_list.append(stock)
    return stock_code_list
