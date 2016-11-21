#program in python 3
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json

def beginScrapyData(baseUrl="http://bidwiz.duapp.com/bwCheckController.do?getBidMonthData",yearStart=2010,yearEnd=2016,maxPages=5,maxPagesize=60):
    for year in range(yearStart,yearEnd+1):
        for month in range(1,13):
            for page in range(1,maxPages):
                bidData = scrapyData(baseUrl,year,month,page,maxPagesize)
                bidData =json.loads(bidData)
                for d in bidData:
                    print(d)


def scrapyData(baseUrl,year,month,page,pageSize=60):
    param={}
    if month<10:
        month="0"+str(month)
    param["bidMonth"]+str(year) + month
    param["page"]=page
    param["rows"]=pageSize
    for key in param:
        baseUrl+="&"+key+"="+param[key]
    
    try:
        html=urlopen(baseUrl)
    except HTTPError as e:
        return None
    
    try:
        bsObj=BeautifulSoup(html.read())
        return bsObj.html.bod.p.get_text()
    except HTTPError as e:
        return None