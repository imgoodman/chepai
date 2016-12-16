from numpy import *
import csv

from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def test():
    with open('../data/ionosphere.data','r') as input_file:
        reader = csv.reader(input_file)
        X = zeros((351,34))
        Y = zeros((351,1))
        for i,row in enumerate(reader):
            data=[float(datum) for datum in row[:-1]]
            X[i] = data
            Y[i] = row[-1]=='g'
        
        X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=14)

        estimator = KNeighborsClassifier()

        estimator.fit(X_train,Y_train)

        Y_predict = estimator.predict(X_test)

        accuracy = mean(Y_test==Y_predict)*100

        print('the accuracy is {0:.1f%}'.format(accuracy))


if __name__=='__main__':
    test()