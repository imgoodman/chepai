import db
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from collections import Counter

import numpy as np
from matplotlib import pyplot as plt

def get_weibo(userId):
    weibos=db.load_weibo_data(userId)
    print(len(weibos))
    # print(weibos)
    n_clusters=10
    #0.4 表示40% 忽略出现在40%及以上的文档中的词语
    pipeline = Pipeline([("feature_extraction",TfidfVectorizer(max_df=0.4)),("cluster",KMeans(n_clusters=n_clusters))])
    pipeline.fit(weibos)
    labels=pipeline.predict(weibos)
    #labels由数字0-9组成的，由n_clusters导致的。
    #labels中的每个数字，表示对应的数据点是属于那个族
    print(labels)
    c=Counter(labels)
    print(c)
    for i in range(n_clusters):
        print("cluster {0} has {1} samples".format(i,c[i]))
    print(pipeline.named_steps['cluster'].inertia_)

def multi_cluster_weibo(userId):
    documents=db.load_weibo_data(userId)
    inertia_scores=[]
    for n in range(2,20):
        cur_inertia_score=[]
        X = TfidfVectorizer(max_df=0.4).fit_transform(documents)
        for i in range(10):
            km=KMeans(n_clusters=n).fit(X)
            cur_inertia_score.append(km.inertia_)
        inertia_scores.append(np.mean(cur_inertia_score))
    print(inertia_scores)
    plt.plot(list(range(2,20)),inertia_scores)
    plt.show()

if __name__=="__main__":
    multi_cluster_weibo("gaoxiaosong")