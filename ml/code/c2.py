from numpy import *
import csv

from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score

def test():
    with open('../data/ionosphere.data','r') as input_file:
        reader = csv.reader(input_file)
        X = zeros((351,34),dtype='float')
        Y = zeros((351,),dtype='bool')#第二个参数为空，表示只有一行
        for i,row in enumerate(reader):
            data=[float(datum) for datum in row[:-1]]
            X[i] = data
            Y[i] = row[-1]=='g'
        print("X is:")
        print(X)
        print("Y is:")
        print(Y)
        
        X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=14)

        estimator = KNeighborsClassifier()

        estimator.fit(X_train,Y_train)

        Y_predict = estimator.predict(X_test)

        accuracy = mean(Y_test==Y_predict)*100

        print('the accuracy is {0:.1f}%'.format(accuracy))

        scores = cross_val_score(estimator,X, Y, scoring='accuracy')
        average_accuracy = mean(scores)*100
        print('the average accuracy is {0:.1f}%'.format(average_accuracy))

        avg_scores=[]
        all_scores=[]
        parameter_values=list(range(1,21))
        for n_neighbors in parameter_values:
            estimator=KNeighborsClassifier(n_neighbors=n_neighbors)
            scores=cross_val_score(estimator,X,Y,scoring='accuracy')

            avg_scores.append(mean(scores))
            all_scores.append(scores)


if __name__=='__main__':
    test()