#program in python 3
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
from time import sleep
import csv
import pymysql

def beginScrapyData(baseUrl="http://bidwiz.duapp.com/bwCheckController.do?getBidHistoricalData",yearStart=2016,yearEnd=2016,maxPages=5,maxPagesize=60):
    allData=[]
    for year in range(yearStart,yearEnd+1):
        for month in range(1,13):
            for page in range(1,maxPages):
                bidData = scrapyData(baseUrl,year,month,page,maxPagesize)
                sleep(5)
                if bidData==None:
                    print("fail to scrapy data")
                    continue
                bidData =json.loads(str(bidData))
                #print(bidData)
                for d in bidData["rows"]:
                    print(d)
                    allData.append(d)
    #saveBidDataToCSV(bidData)
    saveBidDataToDB(allData)


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

def saveBidDataToCSV(bidData,fileName="bidData.csv"):
    csvFile=open("../data/"+fileName,"w+")
    try:
        writer=csv.writer(csvFile)
        writer.writerow(("lowest_price_to","system_time","lowest_price_from","lowest_price","bid_month","lowest_price_time","bid_people_num"))
        for d in bidData["rows"]:
            print(d)
            writer.writerow((d["lowest_price_to"],d["system_time"],d["lowest_price_from"],d["lowest_price"],d["bid_month"],d["lowest_price_time"],d["bid_people_num"]))
    finally:
        csvFile.close()

def saveBidDataToDB(bidData):
    conn=pymysql.connect(host="qdm115145384.my3w.com",user="qdm115145384",passwd="1234atsjtu",db="qdm115145384_db")
    cur=conn.cursor()
    cur.execute("use qdm115145384_db")
    for d in bidData:
        sql="insert into t_bid_data (bid_people_num,system_time,lowest_price_time,bid_month,lowest_price_to,lowest_price,lowest_price_from) values (%d,'%s','%s',%s,%d,%d,%d)" % (d["bid_people_num"],d["system_time"],d["lowest_price_time"],d["bid_month"],d["lowest_price_to"],d["lowest_price"],d["lowest_price_from"])
        print(sql)
        cur.execute(sql)
    cur.close()
    conn.close()

beginScrapyData()