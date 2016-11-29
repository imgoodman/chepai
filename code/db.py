def loadDataSet(fileName='../data/bid_data_all.txt'):
    fr=open(fileName)
    rows=[]
    for line in fr.readlines():
        row=[int(r) for r in line.strip().split('\t')]
        #print(row)
        rows.append(row)
    #print(rows)
    return rows


#loadDataSet()