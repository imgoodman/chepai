import db
import numpy as np
#拆分数据集为训练集合测试集
from sklearn.cross_validation import train_test_split
#实例化分类器
from sklearn.neighbors import KNeighborsClassifier
#交叉验证
from sklearn.cross_validation import cross_val_score
#数据预处理 规范化
from sklearn.preprocessing import MinMaxScaler
#流水线操作
from sklearn.pipeline import Pipeline

def loadData():
    m,n,idArr,dataArr = db.loadOriginalDataSet()
    #print(idArr)
    #print(dataArr)
    X= np.array(dataArr)
    #对数据集进行预处理 将每个特征的值域范围规范化为0-1
    X = MinMaxScaler().fit_transform(X)
    #print(X)
    Y = []
    for row in dataArr:
        if row[3]==row[8]:
            Y.append(True)
        else:
            Y.append(False)
    Y = np.array(Y)
    #print(Y)
    return X,Y

def KNeighborTest():
    X,Y=loadData()
    
    #将数据拆分为训练集和测试集
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state=14)
    
    #实例化
    estimator = KNeighborsClassifier()

    #训练算法
    estimator.fit(X_train,Y_train)

    #预测
    y_predict = estimator.predict(X_test)

    #测试准确率 预处理之前：95.5%； 预处理之后：94.8%
    accuracy = np.mean(Y_test==y_predict)*100
    print("the accuracy is {0:.1f}%".format(accuracy))

    #交叉检验 预处理之前：45.0%；预处理之后：73.2%
    scores = cross_val_score(estimator,X,Y,scoring="accuracy")
    average_accuracy = np.mean(scores)*100
    print("the average accuracy is {0:.1f}%".format(average_accuracy))


def KNeighborMultiTest():
    X,Y=loadData()
    avg_scores=[]
    all_scores=[]
    for n in range(1,21):
        estimator=KNeighborsClassifier(n_neighbors=n)
        scores=cross_val_score(estimator,X,Y,scoring="accuracy")
        avg_scores.append(np.mean(scores))
        all_scores.append(scores)
    print(avg_scores)
    print(all_scores)

def KNeighborPipelineTest():
    X,Y=loadData()
    #传入数组
    #每个数组元素是元祖
    #元祖是（自定义名称，步骤）
    scaling_pipeline=Pipeline([
        ("scale",MinMaxScaler()),
        ("predict",KNeighborsClassifier())
    ])
    scores=cross_val_score(scaling_pipeline,X,Y,scoring="accuracy")
    #71.9%
    print("the pipeline scored an average accuracy for is: {0:.1f}%".format(np.mean(scores)*100))

if __name__=="__main__":
    #KNeighborTest()
    #KNeighborMultiTest()
    KNeighborPipelineTest()