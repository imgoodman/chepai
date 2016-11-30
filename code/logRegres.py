from numpy import *
import db
import dataToFile

def loadDataSet():
    rows=db.loadDataSet()
    dataMat=[]
    labelMat=[]
    for row in rows:
        dMat=[1]
        dMat.extend(row[:-1])
        lMat=row[-1]
        dataMat.append(dMat)
        labelMat.append(lMat)
    #print(mat(dataMat))
    #print(mat(labelMat))
    return mat(dataMat),mat(labelMat)

def sigmoid(inX):
    return 1.0/(1+exp(-inX))

def gradAscent(dataMat,labelMat,maxCycles=500,alpha=0.01):
    labelMat=labelMat.T
    m,n=shape(dataMat)
    weights=ones((n,1))
    for k in range(maxCycles):
        print('the ' +str(k) +'th cycle')
        h=sigmoid(dataMat*weights)
        print("-----h-----")
        print(h)
        error=labelMat-h
        print('-----error-----')
        print(error)
        weights=weights+alpha*dataMat.T*error
        print('----weights-------')
        print(weights)
    return weights,error

if __name__=='__main__':
    dataMat,labelMat=loadDataSet()
    weightMat=[]
    weights,error=gradAscent(dataMat,labelMat,maxCycles=5000)
    print("final weights------")
    print(weights)
    print("final error------")
    print(error)
        #weightMat.append(weights)
    #dataToFile.saveToFile(weightMat)
    #print(weightMat)