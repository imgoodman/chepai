import os
import pandas as pd
import numpy as np
#该转换器可以删除特征值的方差达不到最低标准的特征
from sklearn.feature_selection import VarianceThreshold
#选择单变量特征的转换器，返回k个最佳特征
from sklearn.feature_selection import SelectKBest
#卡方检验 单个特征与某一类别之间的相关性
from sklearn.feature_selection import chi2
from scipy.stats import pearsonr

def test():
    fileName = "../data/adult.data"
    adult = pd.read_csv(fileName,header=None,names=["Age","Work-Class","fnlwgt","Education","Education-Num","Marital-Status","Occupation","Relationship","Race","Sex","Capital-gain","Capital-loss","Hours-per-week","Native-Country","Earnings-Raw"])
    adult.dropna(how='all',inplace=True)
    #print(adult.columns)
    #print(adult["Hours-per-week"].describe())
    #print(adult["Education-Num"].describe())
    #print(adult["Education-Num"].median())
    #print(adult["Work-Class"].unique())
    adult["LongHours"]=adult["Hours-per-week"]>40
    X = adult[["Age","Education-Num","Capital-gain","Capital-loss","Hours-per-week"]].values#返回指定列的值 组成的矩阵
    print(X)
    y = (adult["Earnings-Raw"]=='>50K').values
    print(y)

    # transformer = SelectKBest(score_func=chi2, k=3)#初始化转换器 用卡方函数打分

    # Xt_chi2 = transformer.fit_transform(X,y)
    # print(transformer.scores_)
    # print(Xt_chi2)

    transformer = SelectKBest(score_func=multivariate_pearsonr,k=3)

    Xt_pearsonr = transformer.fit_transform(X,y)
    print(transformer.scores_)


def multivariate_pearsonr(X,y):
    scores,pvalues=[],[]
    for column in range(np.shape(X)[1]):
        cur_score,cur_p = pearsonr(X[:,column],y)
        scores.append(abs(cur_score))
        pvalues.append(cur_p)
    return (np.array(scores),np.array(pvalues))

def testFeature():
    X = np.arange(30).reshape((10,3))
    print(X)
    X[:,1]=1
    print(X)
    vt= VarianceThreshold()
    Xt=vt.fit_transform(X)
    print(Xt)
    print(vt.variances_)


if __name__=='__main__':
    test()