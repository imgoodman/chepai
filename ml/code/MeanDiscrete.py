from sklearn.base import TransformerMixin
from sklearn.utils import as_float_array
import numpy as np

class MeanDiscrete(TransformerMixin):
    def fit(self,X):
        X = as_float_array(X)
        self.mean = X.mean(axis=0)#每一列的均值
        return self

    def transform(self,X):
        X = as_float_array(X)
        assert np.shape(X)[1]==self.mean.shape[0]
        return X>self.mean