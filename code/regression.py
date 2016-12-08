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
    m,n=shape(dataMat)
    print("data is:")
    print(dataMat)
    print("label is:")
    print(labelMat)
    ws = standRegres(dataMat,labelMat)
    print("weights of stand regression")
    print(ws)
    yHat=dataMat*ws
    cor=corrcoef(yHat.T,labelMat)
    print('relate weight')
    print(cor)
    compareData=zeros((m,n+2))
    compareData[:,:n]=dataMat
    for i in range(m):
        compareData[i,n]=exp(labelMat[0][i].A)
        compareData[i,n+1]=exp(dataMat[i]*ws)
    print('compare data is:')
    print(compareData[:,n:])

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
    print('-------lwlr weights-----------')
    print(ws)
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
    yHat01=lwlr(xArr[0],xArr,yArr,0.1)    
    yHat1=lwlr(xArr[0],xArr,yArr,1)    
    yHat10=lwlr(xArr[0],xArr,yArr,10)
    print('-------0.1--------')
    print(yHat01)
    print(exp(yHat01))
    print('-------1--------')
    print(yHat1)
    print(exp(yHat1))
    print('-------10--------')
    print(yHat10)
    print(exp(yHat10))

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
    testStandRegress()