from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV

import numpy as np

iris=load_iris()
X,y = iris.data,iris.target
print('x is:')
print(X.shape)
print(X)
print('y is:')
print(y.shape)
print(y)

pca =PCA(n_components=2)

selection=SelectKBest(k=1)

combined_features=FeatureUnion([('pca',pca),('univ_select',selection)])

X_features = combined_features.fit(X,y).transform(X)

svm=SVC(kernel='linear')

pipeline = Pipeline([('features',combined_features),('svm',svm)])

param_grid = dict(features__pca__n_components=[1,2,3],
                features__univ_select_k=[1,2],
                svm__C=[0.1,1,10])
grid_search = GridSearchCV(pipeline,param_grid=param_grid,verbose=10)
grid_search.fit(X,y)
print(grid_search.best_estimator_)