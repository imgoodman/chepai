def loadDataSet(fileName='../data/bid_data_all.txt'):
    fr=open(fileName)
    rows=[]
    for line in fr.readlines():
        row=[int(r) for r in line.strip().split('\t')]
        row[0]=int(str(row[0])[3:])
        #print(row)
        rows.append(row)
    #print(rows)
    return rows


#loadDataSet()