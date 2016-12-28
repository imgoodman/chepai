import pandas as pd
import db
import numpy as np
from sklearn.feature_selection import VarianceThreshold

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from scipy.stats import pearsonr

def test():
    data=db.loadOriginalDataSetWithPandas()
    #print(data)
    X = data[["system-time","real-lowest-price-time","real-lowest-price",'alert-price','bid-people-num','license-num']].values
    Y = data["result"].values
    #print(X)
    #print(Y)
    #测试方差
    #vt = VarianceThreshold()
    #Xt= vt.fit_transform(X)
    #print(Xt)
    transformer = SelectKBest(score_func=chi2,k=3)
    Xt_chi2 = transformer.fit_transform(X,Y)
    print(transformer.scores_)


if __name__=='__main__':
    test()