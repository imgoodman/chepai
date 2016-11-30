from numpy import *
import db

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
    return mat(dataMat),mat(labelMat)


def standRegres(dataMat,labelMat):
    labelMat=labelMat.T
    xTx=dataMat.T*dataMat
    if linalg.det(xTx) == 0.0:
        print("this matrix is singular, can not be inverse")
        return
    ws=xTx.I * dataMat.T * labelMat
    return ws

def testStandRegress():
    dataMat,labelMat=loadDataSet()
    ws = standRegres(dataMat,labelMat)
    print(ws)
    yHat=dataMat*ws
    cor=corrcoef(yHat.T,labelMat)
    print('relate weight')
    print(cor)
    testData=[1,612,40,87500,86800,220000,11000]
    testData=mat(testData)
    testLabel=testData*ws
    print(testLabel)

def lwlr(testPoint,xArr,yArr,k=1.0):
    yArr=yArr.T
    m=shape(xArr)[0]
    weights=mat(eye((m)))
    for j in range(m):
        diffMat = testPoint - xArr[j,:]
        print(diffMat*diffMat.T)
        weights[j,j]=exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx=xArr.T*weights*xArr
    if linalg.det(xTx)==0.0:
        print("this matrix is singular, can not be inverse")
        return
    ws=xTx.I * xArr.T * weights * yArr
    return testPoint*ws

def lwlrTest(testArr,xArr,yArr,k=1.0):
    m=shape(testArr)[0]
    yHat=zeros(m)
    for i in range(m):
        yHat[i]=lwlr(testArr[i],xArr,yArr,k)
    return yHat

def rssError(yArr,yHatArr):
    print((yArr-yHatArr)**2)
    return ((yArr-yHatArr)**2).sum()

def testLwlr():
    xArr,yArr=loadDataSet()
    print(xArr[0])
    yHat=lwlr(xArr[0],xArr,yArr,0.1)

def compareRegress():
    xArr,yArr=loadDataSet()
    print(xArr[0:10])
    print(yArr[:,0:10])
    yHat01=lwlrTest(xArr[0:10],xArr[0:10],yArr[:,0:10],0.1)
    yHat1=lwlrTest(xArr[0:10],xArr[0:10],yArr[:,0:10],1)
    yHat10=lwlrTest(xArr[0:10],xArr[0:10],yArr[:,0:10],10)
    rssError01=rssError(yArr[:,0:10],yHat01.T)
    rssError1=rssError(yArr[:,0:10],yHat1.T)
    rssError10=rssError(yArr[:,0:10],yHat10.T)
    print(rssError01)
    print(rssError1)
    print(rssError10)

if __name__=='__main__':
    testLwlr()