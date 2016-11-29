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

def gradAscent(dataMat,labelMat,maxCycles=500,alpha=0.001):
    labelMat=labelMat.T
    m,n=shape(dataMat)
    weights=ones((n,1))
    for k in range(maxCycles):
        h=sigmoid(dataMat*weights)
        error=labelMat-h
        weights=weights+alpha*dataMat.T*error
        #print(weights)
    return weights

if __name__=='__main__':
    dataMat,labelMat=loadDataSet()
    weightMat=[]
    for c in range(10,20):
        weights=gradAscent(dataMat,labelMat,c)
        weightMat.append(weights)
    weightMat
    #dataToFile.saveToFile(weightMat)
    print(weightMat)