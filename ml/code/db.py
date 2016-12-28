import csv
import pandas as pd

"""
return sample count, feature count, id array, data array
"""
def loadOriginalDataSet(fileName="../data/30_60_useful_bid_data.csv"):
    dataFile=open(fileName,"r")
    csv_reader = csv.reader(dataFile)
    m,n=(0,0)
    idArr=[]
    dataArr=[]
    labelAttr=[]
    for row in csv_reader:
        #print(row)
        if row[0].isdigit():
            if n==0:
                n=len(row)-1
            m=m+1
            idArr.append(int(row[0]))
            dataArr.append([float(x) for x in row[1:-1]])
            labelAttr.append(row[-1])
    return m,n,idArr,dataArr,labelAttr


def loadOriginalDataSetWithPandas(fileName="../data/30_60_useful_bid_data.csv"):
    dataset = pd.read_csv(fileName,skiprows=[0],names=["id","bid-month","system-time","real-lowest-price-time","real-lowest-price","alert-price","avg-price","bid-people-num","license-num","lowest-price","lowest-price-time","lowest-price-order","result"])
    #print(dataset)
    return dataset