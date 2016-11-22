#program in python 3
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
from time import sleep

def beginScrapyData(baseUrl="http://bidwiz.duapp.com/bwCheckController.do?getBidHistoricalData",yearStart=2010,yearEnd=2016,maxPages=5,maxPagesize=60):
    for year in range(yearStart,yearEnd+1):
        for month in range(1,13):
            for page in range(1,maxPages):
                bidData = scrapyData(baseUrl,year,month,page,maxPagesize)
                sleep(5)
                if bidData==None:
                    print("fail to scrapy data")
                    continue
                bidData =json.loads(str(bidData))
                for d in bidData["rows"]:
                    print(d)


def scrapyData(baseUrl,year,month,page,pageSize=60):
    param={}
    if month<10:
        month="0"+str(month)
    param["bidMonth"]=str(year) + str(month)
    param["page"]=page
    param["rows"]=pageSize
    for key in param:
        baseUrl+="&"+key+"="+str(param[key])

    print("scrapy data from " + baseUrl)
    
    try:
        html=urlopen(baseUrl)
    except HTTPError as e:
        print("can not open " + baseUrl)
        return None
    
    try:
        bsObj=BeautifulSoup(html.read(),"html.parser")
        #print(bsObj)
        return bsObj
    except AttributeError as e:
        print("can not get BeautifulSoup Object from html data")
        return None

beginScrapyData()