import pickle
import os

from sklearn.datasets import load_iris
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import f1_score

import lasagne
from lasagne import layers
from lasagne import updates

from nolearn.lasagne import NeuralNet
from lasagne.nonlinearities import sigmoid,softmax

import theano
import theano.tensor as T

def test_lasagne():
    iris = load_iris()
    X = iris.data.astype(np.float32)#data is the key
    y_true = iris.target.astype(np.int32)#target is the key

    X_train,X_test,y_train,y_text =train_test_split(X, y_true, random_state=14)

    input_layer = lasagne.layers.InputLayer(shape=(10,X.shape[1]))

    hidden_layer = lasagne.layers.DenseLayer(input_layer, num_units=12, nonlinearity=lasagne.nonlinearities.sigmoid)

    output_layer = lasagne.layers.DenseLayer(hidden_layer, num_units=3, nonlinearity=lasagne.nonlinearities.softmax)

    net_input = T.matrix('net_input')
    net_output = output_layer.get_output_for(net_input)
    true_output = T.ivector('true_output')

    loss = T.mean(T.nnet.categorical_crossentropy(net_output,true_output))

    all_params = lasagne.layers.get_all_params(output_layer)

    updates = lasagne.updates.sgd(loss, all_params, learning_rate=0.1)

    train = theano.function([net_input, true_output], loss, updates=updates)

    get_output = theano.function([net_input], net_output)

    for n in range(1000):
        train(X_train, y_train)
    
    y_output = get_output(X_test)

    y_pred = np.argmax(y_output, axis=1)

    print(f1_score(y_text, y_pred))

def test_nolearn():
    iris = load_iris()
    X = iris.data.astype(np.float32)#data is the key
    y_true = iris.target.astype(np.int32)#target is the key

    X_train,X_test,y_train,y_test =train_test_split(X, y_true, random_state=14)

    layers =[
        ('input', layers.InputLayer),
        ('hidden',layers.DenseLayer),
        ('output',layers.DenseLayer)
    ]

    net1 = NeuralNet(layers=layers,input_shape=X.shape, hidden_num_units=100, output_num_units=26, hidden_nonlinearity=sigmoid, output_nonlinearity=softmax, hidden_b=np.zeros((100,), dtype=np.float32), update= updates.momentum, update_learning_rate=0.9, update_momentum=0.1, regression=True, max_epochs=1000)

    net1.fit(X_train,y_train)

    y_pred = net1.predict(X_test)
    y_pred = y_pred.argmax(axis=1)
    assert len(y_pred)==len(X_test)
    if len(y_test.shape)>1:
        y_test=y_test.argmax(axis=1)
    print(f1_score(y_test, y_pred))


data_folder=os.path.join("D:/python/ml-20m/ml-20m/cifar-10-python","cifar-10-batches-py")

def unpickle(filename):
    fullpath=os.path.join(data_folder,filename)
    with open(fullpath,'rb') as inf:
        return pickle.load(inf, encoding="latin1")

def test_pickle():
    batch1 = unpickle("data_batch_1")
    print(batch1)

if __name__=="__main__":
    test_lasagne()