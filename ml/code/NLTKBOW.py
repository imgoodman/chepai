from sklearn.base import TransformerMixin
from nltk import *

class NLTKBOW(TransformerMixin):
    def fit(self,X,y=None):
        return self
    def transform(self,X):
        return [{word : True for word in word_tokenize(document)} for document in X]