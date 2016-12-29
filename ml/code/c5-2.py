import os
from collections import defaultdict
import pandas as pd
import numpy as np

import MeanDiscrete
from numpy.testing import assert_array_equal

from sklearn.decomposition import PCA

def loadData():
    converters = defaultdict(convert_number)

    converters[1558]=lambda x: 1 if x.strip()=="ad." else 0#表示类别

    ads = pd.read_csv('../data/ad.data',header=None,converters=converters)
    # print(ads[1:5])
    X = ads.drop(1558,axis=1).values
    # print(X)
    y = ads[1558]
    # print(y)

    pca = PCA(n_components=5)
    Xd = pca.fit_transform(X)
    print(pca.explained_variance_ratio_)

def convert_number(x):
    try:
        return float(x)
    except ValueError:
        return np.nan


def test_meandiscrete():
    mean_discrete = MeanDiscrete.MeanDiscrete()
    X_test = np.array([
        [0,2],
        [3,5],
        [6,8],
        [9,11],
        [12,14],
        [15,17],
        [18,20],
        [21,23],
        [24,26],
        [27,29]
    ])

    mean_discrete.fit(X_test)

    assert_array_equal(mean_discrete.mean, np.array([13.5,15.5]))

    X_transformed = mean_discrete.transform(X_test)
    X_expected = np.array([
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [1,1],
        [1,1],
        [1,1],
        [1,1],
        [1,1]
    ])

    assert_array_equal(X_transformed, X_expected)
    

if __name__=='__main__':
    test_meandiscrete()