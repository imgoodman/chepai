import csv

"""
return sample count, feature count, id array, data array
"""
def loadOriginalDataSet(fileName="../data/30_60_useful_bid_data.csv"):
    dataFile=open(fileName,"r")
    csv_reader = csv.reader(dataFile)
    m,n=(0,0)
    idArr=[]
    dataArr=[]    
    for row in csv_reader:
        #print(row)
        if row[0].isdigit():
            if n==0:
                n=len(row)
            m=m+1
            idArr.append(int(row[0]))
            dataArr.append([float(x) for x in row[1:]])
    return m,n,idArr,dataArr