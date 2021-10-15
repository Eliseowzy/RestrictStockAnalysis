# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@file: main.py
@time: 9/29/2021
@version: 1.0
"""

from models import kmeans_cluster
from utils import data_loader
from utils import stock_calculator


def get_return_rate():
    stock_calculator.calculate_return_rate(day_slot=90)


def get_basic_eps():
    stock_calculator.calculate_basic_eps()


def train_model():
    dataset = data_loader.load_dataframe_from_csv("../data/cluster_dataset.csv")
    features = dataset[
        ['release_feature', 'release_ratio', '6d_return', '10d_return', '16d_return', '20d_return', '30d_return',
         '60d_return', '90d_return', 'basic_eps']]
    KMeans = kmeans_cluster.k_means(data_set=features)
    KMeans.fit()
    KMeans.save_model()
    print(dataset)


def main():
    # stock_calculator.calculate_return_rate(day_slot=90)
    # stock_calculator.calculate_basic_eps()
    train_model()


if __name__ == "__main__":
    main()
