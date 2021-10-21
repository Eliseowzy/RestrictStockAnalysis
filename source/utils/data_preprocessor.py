# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@function: data preprocessor
@file: data_preprocessor.py
@time: 14/10/2021
@version: 1.0
"""
import pandas as pd

from source.utils import data_loader

pd.set_option('display.max_columns', None)


def get_list_by_column(file_path='dataset.xlsx', column_name='代码'):
    """Get stock name list from a table.
    Returns:
        list 'code': A stock code list.
    """
    df = pd.read_excel(file_path)
    if ".xlsx" in file_path:
        data_loader.load_dataframe_from_excel(file_path)
        stock_code_list = []
        for stock in df[column_name]:
            stock_code_list.append(stock)
        return stock_code_list
    if ".csv" in file_path:
        data_loader.load_dataframe_from_csv(file_path)
        stock_code_list = []
        for stock in df[column_name]:
            stock_code_list.append(stock)
        return stock_code_list
    else:
        return None
