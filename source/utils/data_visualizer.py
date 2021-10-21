# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi, Wu Junyi
@function: data visualizer
@file: data_visualizer.py
@time: 18/10/2021
@version: 1.0
"""

import pandas
import seaborn
from matplotlib import pyplot


def heatmap(data_set: pandas.DataFrame, fontsize=20, heatmap_name="../model_diagrams/heatmap.pdf"):
    pyplot.figure(figsize=(15, 15))
    seaborn.heatmap(data=data_set.corr().round(2), annot=True, cmap='coolwarm', linewidths=0.2, square=True,
                    annot_kws={"fontsize": fontsize})
    pyplot.xticks(fontsize=fontsize)
    pyplot.yticks(fontsize=fontsize)
    pyplot.gcf().axes[-1].tick_params(labelsize=fontsize)
    pyplot.savefig(heatmap_name, transparent=True)
    pyplot.close()
