# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@function: implement models based on model interface
@file: kmeans_cluster.py
@time: 14/10/2021
@version: 1.0
"""

from sklearn.cluster import KMeans

from source.interface import model_interface
from source.utils import data_loader

class k_means(model_interface):
    def __init__(self, init='random', n_clusters=8, max_iter=1000, n_init=100):
        self._name = "k-means"
        self._init = init
        self._max_iter = max_iter
        self._n_clusters = n_clusters
        self._n_init = n_init
        self._model_object = KMeans(n_clusters=self._n_clusters, init=self._init, n_init=self._n_init,
                                    max_iter=self._max_iter)
        self._model_brief = {"name": "k-means", "init": str(self._init), "max_iter": str(self.max_iter),
                             "n_clusters": str(self._n_clusters), "n_init": str(self._n_init)}

    def __str__(self):
        return str(self._model_brief)

    def fit(self, train_set):
        self._model_object.fit(train_set)
