# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@function: implement models based on model interface
@file: k_means_cluster.py
@time: 14/10/2021
@version: 1.0
"""
import joblib
import pandas
from sklearn.cluster import KMeans

from source.interface import model_interface


class k_means(model_interface):
    def __init__(self, data_set: pandas.DataFrame = "", init='random', n_clusters=8, max_iter=1000, n_init=100,
                 min_sse=10000000000000000):
        self._name = "k-means"
        self._data_set = data_set
        self._init = init
        self._max_iter = max_iter
        self._n_clusters = n_clusters
        self._n_init = n_init
        self._min_sse = min_sse
        self._model_object = KMeans(n_clusters=self._n_clusters, init=self._init, n_init=self._n_init,
                                    max_iter=self._max_iter)
        self._predict_result = None
        self._model_brief = {"name": "k-means",
                             "data_set": str(self._data_set),
                             "init": str(self._init),
                             "max_iter": str(self.max_iter),
                             "n_clusters": str(self._n_clusters),
                             "n_init": str(self._n_init),
                             "min_sse": str(self._min_sse)}

    def __str__(self):
        return str(self._model_brief)

    def get_predict_result(self):
        return self._predict_result

    def get_model_brief(self):
        return self._model_brief

    def train(self):
        for _ in range(self._max_iter):
            self._model_object.fit(self._data_set)
            _sse = self._model_object.inertia_
            if _sse < self._min_sse:
                self._min_sse = _sse

    def predict(self, dataset: pandas.DataFrame, features: list, label: str):
        try:
            self._model_object.labels_
        except AttributeError:
            self.train()
        if self._model_object.labels_ is not None:
            features = dataset[features]
            self._predict_result = self._model_object.predict(features)
            dataset["cluster_label"] = self._predict_result
            dataset = dataset.sort_values(by='cluster_label', ascending="False")
            self._predict_result = dataset[[label, 'cluster_label']]

    def save_model(self, model_path="../../model/model.pkl"):
        joblib.dump(self._model_object, model_path)

    def load_model(self, model_path="../../model/model.pkl"):
        self._model_object = None
        self._model_object = joblib.load(model_path)
