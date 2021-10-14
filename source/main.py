# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@file: main.py
@time: 9/29/2021
@version: 1.0
"""

from utils import stock_calculator


# def train_model(model="k_means", data_path="../df.csv"):


def main():
    stock_calculator.calculate_return_rate(day_slot = 90)
    # stock_calculator.calculate_basic_eps()


if __name__ == "__main__":
    main()
