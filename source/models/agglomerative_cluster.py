# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wu Junyi
@function: implement models based on model interface
@file: agglomerative_cluster.py
@time: 14/10/2021
@version: 1.0
"""

import joblib
import pandas
from sklearn.cluster import AgglomerativeClustering

from source.interface import model_interface


class agglomerative_cluster(model_interface.model_interface):
    def __init__(self, data_set: pandas.DataFrame = "", n_clusters=5, affinity='euclidean', linkage='ward'):
        self._data_set = data_set
        self._n_clusters = n_clusters
        self._affinity = affinity
        self._linkage = linkage
        self._model_object = AgglomerativeClustering(n_clusters=self._n_clusters, affinity=self._affinity,
                                                     linkage=self._linkage)
        self._predict_result = None
        self._model_brief = {"name": "agglomerative"}

    def __str__(self):
        return self._model_brief

    def train(self):
        self._model_object.fit(self._data_set)

    def predict(self):
        self._predict_result = self._model_object.labels_

    def save_model(self, model_path="../../models/model.pkl"):
        joblib.dump(self._model_object, model_path)

    def load_model(self, model_path="../../models/model.pkl"):
        self._model_object = None
        self._model_object = joblib.load(model_path)

    def get_model_brief(self):
        return self._model_brief

    def get_predict_result(self):
        if self._predict_result is not None:
            return self._predict_result
        else:
            self.predict()
            return self._predict_result
# data_set = pandas.read_csv("Documents/cluster_dataset.csv")
# data_set = data_set.set_index(["StockName"])
# dt = data_set.iloc[:, 1:]
# test = AGRClassifier()
# test.train(dt.values)
# test.predict()
# dt['labels'] = test.get_predict_result()
