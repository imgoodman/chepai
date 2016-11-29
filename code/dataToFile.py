import json

def saveToFile(data,fileName="dataToFile",fileType="txt"):
    dataFile=open("../data/"+fileName+"."+fileType,'w')
    if fileType=='txt':
        fileContent=''
        for row in data:
            for d in row:
                fileContent+=str(d)+'\t'
            fileContent+='\n'
        dataFile.write(fileContent)
    if fileType=='json':
        dataFile.write(json.dumps(data))
    dataFile.close()