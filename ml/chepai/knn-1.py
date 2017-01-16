import pandas as pd#读取数据集
import numpy as np
from sklearn.preprocessing import MinMaxScaler#数据归一化
from sklearn.cross_validation import train_test_split#数据集切分
from sklearn.cross_validation import cross_val_score#交叉验证
from sklearn.neighbors import KNeighborsClassifier#分类器
from matplotlib import pyplot as plt#反复试验结果差异展示
from sklearn.pipeline import Pipeline#将每个步骤组装起来

def load_dataSet():
    data = pd.read_csv("../data/30_60_useful_bid_data.csv")
    # print("original data set is:")
    # print(data)
    # print("------------------------------original data ends here-------------------------------------------------")
    return data

def get_XY_from_data(data):
    X=data[data.columns[1:-1]]
    Y=data[data.columns[-1]]
    # print('X is:')
    # print(X)
    # print('Y is:')
    # print(Y)
    # print('-------------------------------original X,Y data ends here---------------------------------------------------------------------')
    return (X,Y)

def get_actual_XY_from_data(data):
    X=data[["bid_month","system_time","real_lowest_price","alert_price","bid_people_num","license_num"]]
    Y=data[data.columns[-1]]
    # print('X is:')
    # print(X)
    # print('Y is:')
    # print(Y)
    # print('-------------------------------original X,Y data ends here---------------------------------------------------------------------')
    return (X,Y)

def min_max_X(X):
    X_transformed = MinMaxScaler().fit_transform(X)#注意是fit_transform()，既不是fit()，也不是transform()哦
    print('transformed X is:')
    print(X_transformed)
    print('--------------------------------transformed X ends here---------------------------------------------------------------------------------------')
    return X_transformed

def split_data(X,Y):
    x_train,x_test,y_train,y_test = train_test_split(X,Y,random_state=14)#采样 交叉验证
    print('train x is:{0}'.format(len(x_train)))
    print(x_train)
    print('train y is:{0}'.format(len(y_train)))
    print(y_train)
    print('test x is:{0}'.format(len(x_test)))
    print(x_test)
    print('test y is:{0}'.format(len(y_test)))
    print(y_test)
    print('-------------------------------------sample cross validation ends here-----------------------------------------------------------')
    return x_train,x_test,y_train,y_test

def knn(scoring='accuracy'):
    data=load_dataSet()
    X,Y=get_XY_from_data(data)
    X= min_max_X(X)
    x_train,x_test,y_train,y_test=split_data(X,Y)
    #data is ready
    estimator = KNeighborsClassifier()
    estimator.fit(x_train, y_train)
    y_pred = estimator.predict(x_test)
    print('y predict is:{0}'.format(len(y_pred)))
    print(y_pred)
    print('y test equals y pred ?')
    print(y_test==y_pred)
    accuracy = np.mean(y_test==y_pred)*100
    print('accuracy is: {0:.1f}%'.format(accuracy))

    scores=cross_val_score(estimator, X, Y,scoring=scoring)#准确率
    print('cross validation scores is:{0}'.format(len(scores)))
    print(scores)
    average_score = np.mean(scores)*100
    print('the average accuracy score is: {0:.1f}%'.format(average_score))

def knn_neighbor_num(scoring='accuracy'):
    data=load_dataSet()
    X,Y=get_XY_from_data(data)
    X= min_max_X(X)

    avg_scores=[]
    #data is ready
    for i in range(1,50):
        estimator =KNeighborsClassifier(n_neighbors=i)
        scores=cross_val_score(estimator,X,Y,scoring=scoring)
        print('the scores of {0} is {1}'.format(i ,scores))
        print('the average accuracy of {0} neighbors is:{1:.1f}%'.format(i,np.mean(scores)*100))
        avg_scores.append(np.mean(scores)*100)
    plt.plot(list(range(1,50)),avg_scores)
    plt.show()

def knn_pipeline():
    data=load_dataSet()
    X,Y=get_XY_from_data(data)
    scaling_pipeline= Pipeline([("scaling",MinMaxScaler()),("predict",KNeighborsClassifier())])
    scores = cross_val_score(scaling_pipeline, X, Y, scoring='accuracy')
    print('the average score is: {0:.1f}%'.format(np.mean(scores)*100))

def knn_actual():
    data=load_dataSet()
    X,Y=get_actual_XY_from_data(data)
    scaling_pipeline=Pipeline([("scaling",MinMaxScaler()),("predict",KNeighborsClassifier())])
    scores=cross_val_score(scaling_pipeline,X,Y,scoring="accuracy")
    print("actual average accuracy:{0:.1f}%".format(np.mean(scores)*100))

def actual_pred_by_knn():
    bid_month=17.01
    alert_price=86000
    license_num=12215
    bid_people_num=219882
    # system_time=9.59
    # real_lowest_price=88000
    results=[]
    success_counts=[]
    for t in np.arange(9.30,9.59,0.01):
        for i in range(86000,100000,100):
            data=load_dataSet()
            X,Y=get_actual_XY_from_data(data)
            current_data={'bid_month':bid_month,"system_time":t,"real_lowest_price":i,"alert_price":alert_price,"bid_people_num":bid_people_num,"license_num":license_num}
            print(current_data)
            X.loc[len(X)]=current_data
            # print(X)
            X = min_max_X(X)
            X_data=X[:-1]
            X_new_data=X[-1]
            print('scaled original data is:{0}'.format(len(X_data)))
            print(X_data)
            print('scaled new data is:{0}'.format(len(X_new_data)))
            print(X_new_data)
            estimator =KNeighborsClassifier()
            scores=cross_val_score(estimator,X_data,Y,scoring="accuracy")
            print('the scores is:{0}'.format(len(scores)))
            print(scores)
            print('the average score is:{0:.1f}%'.format(np.mean(scores)*100))
            estimator.fit(X_data,Y)
            y_new_data_pred=estimator.predict(X_new_data)
            print(y_new_data_pred)
            results.append([i,t,y_new_data_pred[0]])
            if y_new_data_pred[0]==1:
                success_counts.append([i,t,y_new_data_pred[0]])
    print(results)
    print(success_counts)

if __name__=="__main__":
    # knn(scoring='f1')
    # knn_neighbor_num()
    # knn_pipeline()
    # knn_actual()
    actual_pred_by_knn()