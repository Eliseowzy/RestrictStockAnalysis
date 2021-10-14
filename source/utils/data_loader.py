# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@function: load external data
@file: data_loader.py
@time: 14/10/2021
@version: 1.0
"""
import pandas as pd


def load_dataframe_from_csv(file_path="../../data/df.csv"):
    dataset = pd.read_csv(file_path)
    # print(dataset)
    return dataset


def load_dataframe_from_excel(file_path=""):
    dataset = pd.read_excel(file_path)
    return dataset


if __name__ == '__main__':
    load_dataframe_from_csv()
