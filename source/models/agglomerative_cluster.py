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
    def __init__(self, data_set: pandas.DataFrame = "", features_list: list = None, label: str = "", n_clusters=5,
                 affinity='euclidean', linkage='ward'):
        self._data_set = data_set
        self._features_list = features_list
        self._label = label
        self._n_clusters = n_clusters
        self._affinity = affinity
        self._linkage = linkage
        self._model_object = AgglomerativeClustering(n_clusters=self._n_clusters, affinity=self._affinity,
                                                     linkage=self._linkage)
        self._predict_result = None
        self._model_brief = {"name": "agglomerative",
                             "features": str(self._features_list),
                             "label": str(self._label),
                             "n_clusters": str(self._n_clusters),
                             "affinity": str(self._affinity),
                             "linkage": str(self._linkage)}

    def __str__(self):
        return str(self._model_brief)

    def train(self):
        features = self._data_set[self._features_list]
        self._model_object.fit(features)

    def predict(self):
        try:
            self._model_object.labels_
        except AttributeError:
            self.train()
        if self._model_object.labels_ is not None:
            features = self._data_set[self._features_list]
            self._predict_result = self._model_object.fit_predict(features)
            self._data_set["cluster_label"] = self._predict_result
            dataset = self._data_set.sort_values(
                by='cluster_label', ascending="False")
            self._predict_result = dataset[[self._label, 'cluster_label']]

    def save_model(self, model_path="../../models/agg_model.pkl"):
        joblib.dump(self._model_object, model_path)

    def load_model(self, model_path="../../models/agg_model.pkl"):
        self._model_object = None

        self._model_object = joblib.load(model_path)
        self._linkage = self._model_object.linkage
        self._affinity = self._model_object.affinity
        self._n_clusters = self._model_object.n_clusters

        self._model_brief["linkage"] = str(self._linkage)
        self._model_brief["label"] = str(self._affinity)
        self._model_brief["n_clusters"] = str(self._n_clusters)
        # self._n_clusters["n_clusters"] = str(self._n_clusters)

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
