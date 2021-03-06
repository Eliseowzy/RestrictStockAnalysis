# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@function: implement models based on model interface
@file: k_means_cluster.py
@time: 20/10/2021
@version: 1.0
"""
import joblib
import numpy
import pandas
import seaborn
from matplotlib import animation
from matplotlib import pyplot
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

from source.interface import model_interface

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pyplot.rcParams['font.sans-serif'] = ['SimHei']
pyplot.rcParams['axes.unicode_minus'] = False


def _prepare_pca(components_count=3, data: pandas.DataFrame = None, kmeans_labels=None):
    names = ['x', 'y', 'z']
    matrix = PCA(n_components=components_count).fit_transform(data)
    df_matrix = pandas.DataFrame(matrix)
    df_matrix.rename({i: names[i] for i in range(components_count)}, axis=1, inplace=True)
    df_matrix['labels'] = kmeans_labels
    return df_matrix


def _prepare_tsne(dimension=3, data: pandas.DataFrame = "", kmeans_labels: list = ""):
    names = ['x', 'y', 'z']
    matrix = TSNE(n_components=dimension, init='pca').fit_transform(data)
    df_matrix = pandas.DataFrame(matrix)
    df_matrix.rename({i: names[i] for i in range(dimension)}, axis=1, inplace=True)
    df_matrix['labels'] = kmeans_labels
    return df_matrix


class k_means(model_interface.model_interface):
    def __init__(self, data_set: pandas.DataFrame = "", features_list: list = None, label: str = "", init='random',
                 n_clusters=8, max_iter=100, n_init=100,
                 min_sse=10000000000000000):
        """k_means class construction function.

        Args:
            data_set (pandas.DataFrame, optional): Dataset. Defaults to "".
            init (str, optional): Initialize method for k_means. Defaults to 'random'.
            features_list (list, optional): [description]. Defaults to None.
            label (str, optional): [description]. Defaults to "".
            n_clusters (int, optional): Number of time the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n_init consecutive runs in terms of inertia. Defaults to 8.
            max_iter (int, optional): [description]. Defaults to 1000.
            n_init (int, optional): [description]. Defaults to 100.
            min_sse (int, optional): [description]. Defaults to 10000000000000000.
        """
        if features_list is None:
            features_list = []
        self._name = "k-means"
        self._data_set = data_set
        self._features_list = features_list
        self._label = label
        self._init = init
        self._max_iter = max_iter
        self._n_clusters = n_clusters
        self._n_init = n_init
        self._min_sse = min_sse
        self._model_object = KMeans(n_clusters=self._n_clusters, init=self._init, n_init=self._n_init,
                                    max_iter=self._max_iter)
        self._predict_result = None
        self._model_brief = {"name": "k-means",
                             # "data_set": str(self._data_set.describe()),
                             "features": str(self._features_list),
                             "label": str(self._label),
                             "init": str(self._init),
                             "max_iter": str(self._max_iter),
                             "n_clusters": str(self._n_clusters),
                             "n_init": str(self._n_init),
                             "min_sse": str(self._min_sse)}

    def __str__(self):
        return str(self._model_brief)

    def get_predict_result(self):
        if self._predict_result is not None:
            return self._predict_result
        else:
            self.predict()
            return self._predict_result

    def get_model_brief(self):
        return self._model_brief

    def train(self):
        features = self._data_set[self._features_list]
        for _ in range(self._max_iter):
            print("iteration {}".format(_))
            self._model_object.fit(features)
            _sse = self._model_object.inertia_
            if _sse < self._min_sse:
                self._min_sse = _sse

    def predict(self):
        try:
            self._model_object.labels_
        except AttributeError:
            self.train()
        if self._model_object.labels_ is not None:
            features = self._data_set[self._features_list]
            self._predict_result = self._model_object.predict(features)
            self._data_set["cluster_label"] = self._predict_result
            dataset = self._data_set.sort_values(
                by='cluster_label', ascending="False")
            dataset.to_excel("../data/data_result.xlsx")
            self._predict_result = dataset[[self._label, 'cluster_label']]

    def save_model(self, model_path="../../models/km_model.pkl"):
        joblib.dump(self._model_object, model_path)

    def load_model(self, model_path="../../models/km_model.pkl"):
        self._model_object = None
        self._model_object = joblib.load(model_path)
        self._init = self._model_object.init
        self._max_iter = self._model_object.max_iter
        self._n_clusters = self._model_object.n_clusters
        self._n_init = self._model_object.n_init

        self._model_brief["init"] = str(self._init)
        self._model_brief["max_iter"] = str(self._max_iter)
        self._model_brief["n_clusters"] = str(self._n_clusters)
        self._model_brief["n_init"] = str(self._n_init)

    def draw_model_selection_diagram(self, max_cluster=20, diagram_name="../model_diagrams/model_selection_kmeans.svg"):
        model_scores = [KMeans(n_clusters=i + 2).fit(self._data_set[self._features_list]).inertia_ for i in
                        range(max_cluster)]
        cluster_cont = numpy.arange(2, self._max_iter + 2)
        seaborn.lineplot(cluster_cont, model_scores)
        print(cluster_cont)
        print(model_scores)
        pyplot.xlabel('????????????')
        pyplot.ylabel("????????????")
        pyplot.title("K-Means???????????????-????????????")
        pyplot.savefig(fname=diagram_name)

        pyplot.close()

    def draw_pca_scatter(self, components_count=3, scatter_name="../model_diagrams/pca_scatter.svg"):
        pca_df = _prepare_pca(components_count=components_count, data=self._data_set[self._features_list],
                              kmeans_labels=self._model_object.labels_)
        seaborn.scatterplot(x=pca_df.x, y=pca_df.y, hue=pca_df.labels, palette="Set1")

        pyplot.savefig(fname=scatter_name, tansprint=True)
        pyplot.close()

    def draw_pca_3d_scatter(self, scatter_name="../model_diagrams/pca_scatter_3d.gif"):
        tsne_pca_df_3d = _prepare_tsne(dimension=3, data=self._data_set[self._features_list],
                                       kmeans_labels=self._model_object.labels_)

        def update(num):
            ax.view_init(200, num)

        N = 360
        fig = pyplot.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(tsne_pca_df_3d['x'], tsne_pca_df_3d['y'], tsne_pca_df_3d['z'],
                   c=tsne_pca_df_3d['labels'],
                   s=6, depthshade=True, cmap='Paired')
        ax.set_zlim(-15, 25)
        ax.set_xlim(-20, 20)
        pyplot.tight_layout()
        ani = animation.FuncAnimation(fig, update, N, blit=False, interval=50)
        ani.save(filename=scatter_name, writer='imagemagick')
        pyplot.show()
        pyplot.close()
