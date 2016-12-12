import math
def loadDataSet(fileName='../data/bid_data_all.txt'):
    fr=open(fileName)
    rows=[]
    for line in fr.readlines():
        r=line.strip().split('\t')
        row=[int(r[0]),math.log(int(str(r[1])[3:]))]
        row.extend([math.log(int(x)) for x in r[2:]])
        #row=[math.log(int(r)) for r in line.strip().split('\t')]
        #row[0]=int(str(row[0])[3:])
        #print(row)
        rows.append(row)
    #print(rows)
    return rows


#loadDataSet()