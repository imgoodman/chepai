import pandas as pd
import db
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score

from sklearn.feature_selection import VarianceThreshold

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from scipy.stats import pearsonr

def test():
    data=db.loadOriginalDataSetWithPandas()
    #print(data)
    # print(data["alert-price"].describe())
    X = data[["system-time","real-lowest-price-time","real-lowest-price",'alert-price','bid-people-num','license-num']].values
    Y = data["result"].values
    #print(X)
    #print(Y)
    #测试方差
    # vt = VarianceThreshold()
    # Xt= vt.fit_transform(X)
    # print(Xt)
    #卡方检验
    transformer_chi = SelectKBest(score_func=chi2,k=3)
    Xt_chi2 = transformer_chi.fit_transform(X,Y)
    print(transformer_chi.scores_)#未经过归一化，结果显示，”实时实际最低价，警示价，参拍人数和拍卖额度“是最佳特征。这个结果值得商榷

    #pearsonr检验
    transformer_pearsonr=SelectKBest(score_func=multivariate_pearsonr, k=3)
    Xt_pearsonr=transformer_pearsonr.fit_transform(X,Y)
    print(transformer_pearsonr.scores_)#通过pearsonr检验，发现，“系统时间，实时最低价时间，实时最低价，警示价，参拍人数,额度”是最佳特征，score差距不大

    #看那个特征集合效果更好
    clf=DecisionTreeClassifier(random_state=14)
    scores_chi2 = cross_val_score(clf,Xt_chi2,Y, scoring='accuracy')
    print(scores_chi2.mean())#0.49
    scores_pearsonr=cross_val_score(clf,Xt_pearsonr,Y,scoring='accuracy')
    print(scores_pearsonr.mean())#0.7 效果更好  说明这6个特征都是重要的

def multivariate_pearsonr(X,y):
    scores,pvalues=[],[]
    for column in range(np.shape(X)[1]):
        cur_score,cur_p=pearsonr(X[:,column],y)
        scores.append(abs(cur_score))
        pvalues.append(cur_p)
    return np.array(scores),np.array(pvalues)


if __name__=='__main__':
    test()