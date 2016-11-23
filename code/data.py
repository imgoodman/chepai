#program in python 3
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
from time import sleep
import csv
import pymysql
import confidentials

def beginScrapyData(baseUrl="http://bidwiz.duapp.com/bwCheckController.do?getBidHistoricalData",yearStart=2013,yearEnd=2013,maxPages=5,maxPagesize=60):
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


def scrapySummaryData(page=1,rows=60):
    url="http://bidwiz.duapp.com/bwCheckController.do?getBidSummaryData&page="+str(page)+"&rows="+str(rows)
    try:
        html=urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bsObj=BeautifulSoup(html.read(),"html.parser")
        summaryData=json.loads(str(bsObj))
        #for d in summaryData["rows"]:
         #   print(d)
        saveSummaryToDB(summaryData)
        return bsObj
    except AttributeError as e:
        return None

def saveSummaryToDB(summaryData):
    secrets=confidentials.getMySqlAuth()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    conn.set_charset("utf8")
    cur=conn.cursor()    
    cur.execute("use "+secrets[3])
    cur.execute("set names utf8;")
    cur.execute("set character set utf8;")
    cur.execute("set character_set_connection=utf8;")
    for d in summaryData["rows"]:
        if d["alert_price"]==None:
            d["alert_price"]=0
        sql="insert into t_bid_summary (bid_month,bid_date,alert_price,avg_price,bid_people_num,bid_percent,license_num,lowest_price,lowest_price_time) values ('%s','%s',%d,%d,%d,'%s',%d,%d,'%s')" % (d["bid_month"],d["bid_date"],d["alert_price"],d["avg_price"],d["bid_people_num"],d["bid_percent"],d["license_num"],d["lowest_price"],d["lowest_price_time"])
        #sql=sql.encode("utf-8")
        print(sql)
        cur.execute(sql)
        #print("insert the following data to database")
        #print(d)
    cur.close()
    conn.close()

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
    secrets=confidentials.getMySqlAuth()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    cur=conn.cursor()
    cur.execute("use "+secrets[3])
    for d in bidData:
        sql="insert into t_bid_data (bid_people_num,system_time,lowest_price_time,bid_month,lowest_price_to,lowest_price,lowest_price_from) values (%d,'%s','%s',%s,%d,%d,%d)" % (d["bid_people_num"],d["system_time"],d["lowest_price_time"],d["bid_month"],d["lowest_price_to"],d["lowest_price"],d["lowest_price_from"])
        print(sql)
        cur.execute(sql)
        #print("save the following dara to database:")
        #print(d)
    cur.close()
    conn.close()

def getJsonFromSummaryData():
    secrets=confidentials.getMySqlAuth()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    cur=conn.cursor()
    cur.execute("use "+secrets[3])
    result=[]
    sql="select * from t_bid_summary order by bid_month asc"
    cur.execute(sql)
    rows=cur.fetchall()
    for r in rows:
        print(r)
        res={}
        res["bid_month"]=r[0]
        res["alert_price"]=r[2]
        res["lowest_price"]=r[7]
        res["avg_price"]=r[3]
        res["bid_people_num"]=r[4]
        res["license_num"]=r[6]
        print(res)
        result.append(res)
    cur.close()
    conn.close()
    file_object=open("../data/summary.json","w")
    file_object.write(json.dumps(result))
    file_object.close()

#beginScrapyData()
#scrapySummaryData()
getJsonFromSummaryData()