# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Wang Zhiyi
@function: data visualizer
@file: data_visualizer.py
@time: 18/10/2021
@version: 1.0
"""

import numpy as np
import pandas
import seaborn
from matplotlib import pyplot


def heatmap(dataframe: pandas.DataFrame):
    pyplot.figure(figsize=(15, 15))
    seaborn.heatmap(data=dataframe.corr().round(2), annot=True, cmap='coolwarm', linewidths=0.2, square=True)
    pyplot.savefig("../model_diagrams/heatmap.svg")
    pyplot.show()

