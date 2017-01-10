import pickle
import os

from sklearn.datasets import load_iris
import numpy as mp
from sklearn.cross_validation import train_test_split

import lasagne

data_folder=os.path.join("D:/python/ml-20m/ml-20m/cifar-10-python","cifar-10-batches-py")

def unpickle(filename):
    fullpath=os.path.join(data_folder,filename)
    with open(fullpath,'rb') as inf:
        return pickle.load(inf, encoding="latin1")

def test_lasagne():
    iris = load_iris()
    X = iris.data.astype(np.float32)#data is the key
    y_true = iris.target.astype(np.int32)#target is the key

    X_train,X_test,y_train,y_text =train_test_split(X, y_true, random_state=14)

    input_layer = lasagne.layers.InputLayer(shape=(10,X.shape[1]))

    hidden_layer = lasagne.layers.DenseLayer(input_layer, num_units=12, nonlinearity=lasagne.nonlinearities.sigmoid)

    output_layer = lasagne.layers.DenseLayer(hidden_layer, num_units=3, nonlinearity=lasagne.nonlinearities.softmax)

if __name__=="__main__":
    batch1 = unpickle("data_batch_1")
    print(batch1)