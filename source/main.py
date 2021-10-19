# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@file: main.py
@time: 9/29/2021
@version: 1.0
"""

from models import agglomerative_cluster
from models import kmeans_cluster
from utils import data_loader
from utils import data_visualizer
from utils import stock_calculator


def get_return_rate():
    stock_calculator.calculate_return_rate(day_slot=90)


def get_basic_eps():
    stock_calculator.calculate_basic_eps()


def train_model(model_name: str = ""):
    data_set = data_loader.load_dataframe_from_csv("../data/cluster_dataset.csv")
    feature_list = ['release_feature', 'release_ratio', '6d_return', '10d_return',
                    '16d_return', '20d_return', '30d_return',
                    '60d_return', '90d_return', 'basic_eps']

    label = "StockName"
    data_visualizer.heatmap(data_set[feature_list])
    if model_name == "km":
        KMeans = kmeans_cluster.k_means(data_set=data_set, init='random',
                                        features_list=feature_list, label=label, n_clusters=5, max_iter=20, n_init=100,
                                        min_sse=10000000000000000)
        KMeans.train()
        KMeans.save_model(model_path="../models/model_kmeans.pkl")
        KMeans.load_model(model_path="../models/model_kmeans.pkl")

        # KMeans.predict()
        KMeans.draw_model_selection_diagram(max_cluster=20, diagram_name="../model_diagrams/model_selection_kmeans.svg")
        KMeans.draw_pca_scatter(components_count=3, scatter_name="../model_diagrams/pca_scatter.svg")
        print(KMeans.get_model_brief())
        print(KMeans.get_predict_result())
    if model_name == "agg":
        Agg = agglomerative_cluster.agglomerative_cluster(data_set=data_set, features_list=feature_list, label=label,
                                                          n_clusters=5,
                                                          affinity="euclidean", linkage="ward")
        Agg.train()
        Agg.save_model(model_path="../models/model_agg.pkl")
        Agg.load_model(model_path="../models/model_agg.pkl")
        Agg.predict()
        Agg.draw_hierarchy_diagram()
        print(Agg.get_model_brief())
        print(Agg.get_predict_result())


def main():
    # stock_calculator.calculate_return_rate(day_slot=90)
    # stock_calculator.calculate_basic_eps()
    train_model(model_name="km")
    # train_model()


if __name__ == "__main__":
    main()
