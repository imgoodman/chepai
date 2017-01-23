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
    terms = pipeline.named_steps["feature_extraction"].get_feature_names()

    print(labels)
    c=Counter(labels)
    print(c)
    for i in range(n_clusters):
        print("cluster {0} has {1} samples".format(i,c[i]))
        print('most important terms:')
        centroid=pipeline.named_steps['cluster'].cluster_centers_[i]#数组 每个族的质心
        most_important = centroid.argsort()
        for i in range(5):
            term_index = most_important[-(i+1)]
            print('{0}  {1} (score: {2:.4f})'.format(i+1,terms[term_index],centroid[term_index]))
    print(pipeline.named_steps['cluster'].inertia_)    

def multi_cluster_weibo(userId):
    documents=db.load_weibo_data(userId)
    inertia_scores=[]
    for n in range(2,20):
        cur_inertia_score=[]
        X = TfidfVectorizer(max_df=0.4).fit_transform(documents)        
        for i in range(10):
            km=KMeans(n_clusters=n).fit(X)
            print('inertia of {0}th in {1} cluster is :{2}'.format(i,n,km.inertia_))
            cur_inertia_score.append(km.inertia_)
        inertia_scores.append(np.mean(cur_inertia_score))
    print(inertia_scores)
    plt.plot(list(range(2,20)),inertia_scores)
    plt.show()

if __name__=="__main__":
    get_weibo("gaoxiaosong")