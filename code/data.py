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

def scrapyDataOfMonth(baseUrl="http://bidwiz.duapp.com/bwCheckController.do?getBidHistoricalData",year=2016,month=12,maxPages=5,maxPageSize=60):
    allData=[]
    for page in range(1,maxPages):
        bidData=scrapyData(baseUrl,year,month,page,maxPageSize)
        sleep(5)
        if bidData==None:
            print("fail to scrapy data")
            continue
        bidData =json.loads(str(bidData))
        #print(bidData)
        for d in bidData["rows"]:
            #print(d)
            allData.append(d)
    return allData

def scrapySummaryDataOfMonth(baseUrl="http://bidwiz.duapp.com/bwCheckController.do?getBidSummaryData",year=2016,month=12,maxPage=1,pageSize=60):
    bidSummaryData = scrapyData(baseUrl,year,month,1,pageSize)
    if month<10:
        month="0"+str(month)
    bid_month=str(year)+str(month)
    #print(bidSummaryData)
    if bidSummaryData!=None:
        bidSummaryData=json.loads(str(bidSummaryData))
        for d in bidSummaryData["rows"]:
            if str(d["bid_month"])==bid_month:
                return d
                # return {
                #     bid_month:bid_month,
                #     bid_date:d["bid_date"],
                #     alert_price:float(d["alert_price"]),
                #     avg_price:float(d["avg_price"]),
                #     bid_people_num:int(d["bid_people_num"]),
                #     bid_percent:d["bid_percent"],
                #     license_num:int(d["license"]),
                #     lowest_price:int(d["lowest_price"]),
                #     lowest_price_time:d["lowest_price_time"]
                # }
                #break

def saveNewestMonthData(year=2016,month=12,maxPage=5,pageSize=60):
    bidSummaryData = scrapySummaryDataOfMonth("http://bidwiz.duapp.com/bwCheckController.do?getBidSummaryData",year,month,maxPage,pageSize)
    bidData = scrapyDataOfMonth("http://bidwiz.duapp.com/bwCheckController.do?getBidHistoricalData",year,month,maxPage,pageSize)    
    secrets=confidentials.getMySqlAuth()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    conn.set_charset("utf8")
    cur=conn.cursor()
    cur.execute("set names utf8;")
    cur.execute("set character set utf8;")
    cur.execute("set character_set_connection=utf8;")
    print(bidSummaryData)
    
    sql="insert into t_bid_summary (bid_month,bid_date,alert_price,avg_price,bid_people_num,bid_percent,license_num,lowest_price,lowest_price_time) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(
        bidSummaryData["bid_month"],bidSummaryData["bid_date"],bidSummaryData["alert_price"],bidSummaryData["avg_price"],bidSummaryData["bid_people_num"],bidSummaryData["bid_percent"],bidSummaryData["license_num"],bidSummaryData["lowest_price"],bidSummaryData["lowest_price_time"]
    )
    print(sql)
    cur.execute(sql)
    if bidData!=None:
        for d in bidData:
            sql="insert into t_bid_data (system_time,lowest_price_time,bid_month,lowest_price_to,lowest_price,lowest_price_from) values ('{0}','{1}','{2}','{3}','{4}','{5}')".format(
                d["system_time"],d["lowest_price_time"],d["bid_month"],d["lowest_price_to"],d["lowest_price"],d["lowest_price_from"]
            )
            print(sql)
            cur.execute(sql)
    cur.close()
    conn.close()


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

"""
save all bid data including summary to csv file
"""
def saveAllBidDataToCSV(fileName,startTime,endTime):
    secrets=confidentials.getMySqlAuth()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    conn.set_charset("utf8")
    cur=conn.cursor()
    cur.execute("set names utf8;")
    cur.execute("set character set utf8;")
    cur.execute("set character_set_connection=utf8;")
    sql='select b.id,b.system_time,b.lowest_price_time as real_lowest_price_time,b.lowest_price as real_lowest_price,b.lowest_price_from as real_lowest_price_from,b.lowest_price_to as real_lowest_price_to,a.bid_date,a.alert_price,a.avg_price,a.bid_people_num,a.bid_percent,a.license_num,a.lowest_price,a.lowest_price_time,a.lowest_price_time as tmp from t_bid_summary as a left join t_bid_data as b on a.bid_month=b.bid_month where 1=1 '
    if startTime!=None:
        sql+=' and system_time>="'+startTime+'"'
    if endTime!=None:
        sql+=' and system_time<="'+endTime+'"'
    sql+=' ORDER BY a.bid_month desc,b.system_time ASC'
    cur.execute(sql)
    csvFile = open("../data/"+fileName,"w+",newline='')
    writer=csv.writer(csvFile)
    writer.writerow(("id","bid_month","system_time","real_lowest_price_time","real_lowest_price","real_lowest_price_from","real_lowest_price_to","bid_date","alert_price","avg_price","bid_people_num","bid_percent","license_num","lowest_price","lowest_price_time","lowest_price_time_order"))
    rows=cur.fetchall()
    for row in rows:
        print(row)
        if row[0]!=None:
            row=list(row)
            lowest_price_time=str(row[len(row)-1])
            lowest_price_time_1=lowest_price_time[:8]
            lowest_price_time_2=lowest_price_time[10:-1]
            #print(lowest_price_time_1+":::::"+lowest_price_time_2)
            row[len(row)-2]=lowest_price_time_1
            row[len(row)-1]=lowest_price_time_2
            writer.writerow(row)
    csvFile.close()
    cur.close()
    conn.close()

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

def getBidDataFromDB(yearStart=2016,yearEnd=2016):
    secrets=confidentials.getMySqlAuth()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    cur=conn.cursor()
    cur.execute('use ' + secrets[3])
    for year in range(yearStart,yearEnd+1):        
        data=''
        for month in range(1,13):
            if month<10:
                month="0"+str(month)
            bid_month=str(year)+str(month)
            sql='select count(0) from t_bid_data where bid_month="%s"' % (bid_month)
            cur.execute(sql)
            r=cur.fetchone()
            if r[0]==0:
                print('no data from ' +bid_month)
                continue
            for second in range(30,60):
                system_time='11:29:'+str(second)
                sql='select lowest_price from t_bid_data where bid_month="%s" and system_time="%s"' % (bid_month,system_time)
                cur.execute(sql)
                r=cur.fetchone()
                lowest_price=0
                if cur.rowcount>0:
                    lowest_price=r[0]
                else:
                    print(bid_month+' '+system_time+' no data ')
                print(bid_month+' '+system_time+' '+str(lowest_price))
                data+=bid_month+'\t'+system_time+'\t'+str(lowest_price)+'\n'
        file_bid_data=open('../data/bid_'+str(year)+'.txt','w')
        file_bid_data.write(data)
        file_bid_data.close()

def getBidDataJsonFromDB(yearStart=2014,yearEnd=2016):
    secrets=confidentials.getMySqlAuth()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    cur=conn.cursor()
    cur.execute('use ' + secrets[3])
    for year in range(yearStart,yearEnd+1):        
        data={}
        data["months"]=[]
        data["rows"]=[]
        for month in range(1,13):
            if month<10:
                month="0"+str(month)
            bid_month=str(year)+str(month)
            sql='select count(0) from t_bid_data where bid_month="%s"' % (bid_month)
            cur.execute(sql)
            r=cur.fetchone()
            if r[0]==0:
                print('no data from ' +bid_month)
                continue
            data["months"].append(bid_month)
            for second in range(30,60):
                system_time='11:29:'+str(second)
                sql='select lowest_price,stand_regress_value,final_margin_price from t_bid_data where bid_month="%s" and system_time="%s"' % (bid_month,system_time)
                cur.execute(sql)
                r=cur.fetchone()
                lowest_price=0
                stand_regress_value=0
                if cur.rowcount>0:
                    lowest_price=r[0]
                    stand_regress_value=int(r[1])
                else:
                    print(bid_month+' '+system_time+' no data ')
                print(bid_month+' '+system_time+' '+str(lowest_price)+' '+str(stand_regress_value))
                data["rows"].append({"bid_month":bid_month,"system_time":system_time,"lowest_price":lowest_price,"stand_regress_value":stand_regress_value,"final_margin_price":r[2]})
        file_bid_data=open('../data/bid_'+str(year)+'.json','w')
        file_bid_data.write(json.dumps(data))
        file_bid_data.close()

def getAllBidData():
    secrets=confidentials.getMySqlAuth()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    cur=conn.cursor()
    cur.execute('use ' +secrets[3])
    sql='select a.bid_month,a.system_time,a.lowest_price,b.alert_price,b.bid_people_num,b.license_num,b.lowest_price as final_lowest_price,a.id from t_bid_data as a left join t_bid_summary as b on a.bid_month=b.bid_month where b.alert_price>0 and a.system_time>="11:29:30" and a.system_time<="11:29:59" order by a.bid_month desc,a.system_time asc'
    cur.execute(sql)
    data=''
    rows=cur.fetchall()
    for r in rows:
        print(r)
        t=r[1].split(':')[2]
        data+=str(r[7])+'\t'+r[0]+'\t'+t+'\t'+str(r[2])+'\t'+str(r[3])+'\t'+str(r[4])+'\t'+str(r[5])+'\t'+str(r[6])+'\n'
    data_file=open('../data/bid_data_all.txt','w')
    data_file.write(data)
    data_file.close()
    cur.close()
    conn.close()


def getJsonOfPriceTimeOfYear(year=2016):
    secrets=confidentials.getMySqlAuth()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    cur=conn.cursor()
    data=[]
    for i in range(1,13):
        if i<10:
            i='0'+str(i)
        bid_month=str(year)+str(i)
        sql='select system_time,lowest_price,stand_regress_value from t_bid_data where system_time>="11:29:30" and system_time<="11:29:59" and bid_month="'+bid_month+'" order by system_time asc'
        cur.execute(sql)
        if cur.rowcount>0:
            d={}
            d["bid_month"]=bid_month
            d["rows"]=[]
            rows=cur.fetchall()
            for row in rows:
                d["rows"].append({"system_time":row[0],"lowest_price":row[1],"stand_regress_value":int(row[2])})
            data.append(d)
    data_file=open('../data/bid_'+str(year)+'_time_price.json','w')
    data_file.write(json.dumps(data))
    cur.close()
    conn.close()


def calculateFinalMarginPrice(year=2014):
    secrets=confidentials.getMySqlAuth()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    cur=conn.cursor()
    for month in range(1,13):
        if month<10:
            month="0"+str(month)
        bid_month=str(year)+str(month)
        sql='select lowest_price from t_bid_data where bid_month=%s and system_time="11:29:59"' % (bid_month)
        cur.execute(sql)
        if cur.rowcount>0:
            final_lowest_price=float(cur.fetchone()[0])

            for t in range(30,59):
                system_time='11:29:'+str(t)
                sql='select lowest_price from t_bid_data where bid_month="%s" and system_time="%s"' % (bid_month,system_time)
                print(sql)
                cur.execute(sql)
                if cur.rowcount>0:
                    t_lowest_price=float(cur.fetchone()[0])
                    margin_price=final_lowest_price - t_lowest_price
                    sql='update t_bid_data set final_margin_price=%f where bid_month="%s" and system_time="%s"' % (margin_price,bid_month,system_time)
                    print(sql)
                    cur.execute(sql)
    cur.close()
    conn.close()

#beginScrapyData()
#scrapySummaryData()
#getJsonFromSummaryData()
#getBidDataFromDB(yearStart=2013,yearEnd=2016)
#getBidDataJsonFromDB(yearStart=2014,yearEnd=2016)
#getAllBidData()
#getJsonOfPriceTimeOfYear(year=2014)
#calculateFinalMarginPrice()
#scrapyDataOfMonth()
#scrapySummaryDataOfMonth()
#saveNewestMonthData()
saveAllBidDataToCSV(fileName="30_60_bid_data.csv",startTime="11:29:30",endTime="11:30:00")