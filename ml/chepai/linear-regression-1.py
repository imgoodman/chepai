import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression,Ridge
from sklearn.cross_validation import train_test_split,cross_val_score

"""
get bid detail data (the last 30 seconds: from 29:30-30:00)
"""
def load_dataset():
    return pd.read_csv("../data/30_60_useful_bid_data.csv")

"""
get bid summary data of  each month
"""
def load_dataset_summary():
    return pd.read_csv("../data/summary.csv")

"""
get X,y from bid detail data
returns bid_month,system_time,alert_price,bid_people_num,license_num
and lowest_price
"""
def get_XY():
    data=load_dataset()
    X=data[["bid_month","system_time","alert_price","bid_people_num","license_num"]]
    Y=data[["lowest_price"]]
    return X,Y

def get_XY_summary():
    data=load_dataset_summary()
    month=data["bid_month"]
    X=data[["alert_price","bid_people_num","license_num"]]
    y=data["lowest_price"]
    return X,y,month

def linear_regress_lowest_price():
    X,y,month=get_XY_summary()
    x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=14)
    reg=LinearRegression(normalize=False,copy_X=True,n_jobs=1,fit_intercept=True)
    reg.fit(x_train,y_train)
    print(reg.coef_)
    plt.xticks(range(len(month)))
    plt.plot(range(len(month)),y)
    plt.plot(range(len(month)),reg.predict(X))
    plt.show()

def linear_regression_real_lowest_price():
    data=load_dataset()
    month=data[["bid_month"]]
    X=data[data["system_time"]>=9.40][["system_time","alert_price","bid_people_num","license_num"]]
    y=data[data["system_time"]>=9.40][["real_lowest_price"]]
    x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=14)
    reg=LinearRegression()
    reg.fit(x_train,y_train)
    print(reg.coef_)
    # print(reg.predict(x_test))
    y_pred=reg.predict(X)
    y["pred"]=y_pred
    # print(y)
    # plt.scatter(data[["system_time"]],y_pred,c='red')
    # plt.scatter(data[["system_time"]],y,c='green')
    # plt.show()
    #某月，29：30秒到29：60秒的实际最低价与预测最低价
    x_month=X[month["bid_month"]==17.01]["system_time"]
    # print(x_month)
    y_month=y[month["bid_month"]==17.01]
    print(y_month)
    plt.xticks(range(len(x_month)))
    plt.plot(range(len(x_month)),y_month["real_lowest_price"])
    plt.plot(range(len(x_month)),y_month["pred"])
    plt.legend()
    plt.show()

def linear_regression_price_margin():
    data=load_dataset()
    X=data[["system_time","alert_price","license_num","bid_people_num"]]
    y=data[["real_lowest_price"]]
    y["margin"]=y["real_lowest_price"]-data["alert_price"]
    # print(y)
    # print(y.describe())
    reg=LinearRegression()
    x_train,x_test,y_train,y_test=train_test_split(X,y["margin"],random_state=14)
    reg.fit(x_train,y_train)
    print(reg.coef_)
    y["pred"]=reg.predict(X)
    
    x_month=X[data["bid_month"]==16.12]["system_time"]
    y_month=y[data["bid_month"]==16.12]["margin"]
    y_month_pred=y[data["bid_month"]==16.12]["pred"]
    # print(x_month)
    # print(y_month)
    # print(y_month_pred)
    plt.xticks(range(len(x_month)))
    plt.plot(range(len(x_month)),y_month)
    plt.plot(range(len(x_month)),y_month_pred)
    plt.legend()
    plt.show()
    # print(reg.predict(x_test)-y_test)
    # scores=cross_val_score(reg,X,y,scoring='accuracy')
    # print(scores)

def ridge_regression():
    X,y=get_XY()
    x_train,x_test,y_train,y_test=train_test_split(X,y,random_state=14)
    reg=Ridge(alpha=0.5,fit_intercept=True,normalize=False,copy_X=True,max_iter=None,tol=1e-3,solver="auto",random_state=None)
    reg.fit(x_train,y_train)
    print(reg.coef_)
    print(reg.intercept_)

if __name__=="__main__":
    linear_regression_price_margin()