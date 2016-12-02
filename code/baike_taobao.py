import pymysql
import io
import sys
import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from time import sleep

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

def getItemInBaikeByUrl(url='http://baike.baidu.com/item/%E7%94%B5%E7%BC%86'):
    try:
        html=urlopen(url)
    except HTTPError as e:
        print("can not open " +url)
        return None
    
    try:
        bsObj=BeautifulSoup(html.read(),'html.parser')
        return bsObj
    except AttributeError as e:
        print("can not get BeautifulSoup object from html of " + url)
        return None

def getChildViews(bsObj,url):
    try:
        item_data={}
        #main content
        #child views
        main_content=bsObj.findAll("div",{"class":"main-content"})[0]

        title=main_content.findAll("dd",{"class":"lemmaWgt-lemmaTitle-title"})[0].h1.get_text()
        item_data["title"]=title
        item_data["url"]=url

        item_data["child_views"]=[]

        paragraphs=main_content.findAll("div",{"class":"para"})
        for para in paragraphs:
            view_url=para.findAll("a",{"href":re.compile("\/view\/[0-9]+\.htm")})
            for link in view_url:
                item_data["child_views"].append({"title":link.get_text(),"href":link["href"]})
        
        #side content
        #image and relate views
        side_content=bsObj.findAll("div",{"class":"side-content"})[0]

        summary_pic=side_content.findAll("div",{"class":"summary-pic"})[0]
        img_url=summary_pic.a.img["src"]
        item_data["img_url"]=img_url
        
        return item_data
    except:
        return None

def saveBaikeItem(item_data):
    try:
        conn=pymysql.connect(host='192.168.1.5',user='root',passwd='sdsdsdsd',db='idea')
        conn.set_charset('utf8')
        cur=conn.cursor()
        cur.execute('set names utf8;')
        cur.execute('set character set utf8;')
        cur.execute('set character_set_connection=utf8;')
        sql="select count(0) from t_baike where title='"+item_data["title"]+"'"
        cur.execute(sql)
        if cur.fetchone()[0]==0:
            sql="insert into t_baike (title,img_url,url) values ('%s','%s','%s')" % (item_data["title"],item_data["img_url"],item_data["url"])
            cur.execute(sql)
            conn.commit()
            id=cur.lastrowid

            values=[]
            for child in item_data["child_views"]:
                values.append((id,child["title"],child["href"]))
            sql="insert into t_baike_child (baike_id,title,url) values (%s,%s,%s)"
            cur.executemany(sql,values)
            conn.commit()
            print("save to database successfully " + str(id))
        else:
            sql="select id from t_baike where title='"+item_data["title"]+"' limit 1"
            cur.execute(sql)
            id=cur.fetchone()[0]
            print('get item from database '+str(id))
        cur.close()
        conn.close()    
        return id
    except:
        return None

def isTitleScrapyed(title):
    try:
        conn=pymysql.connect(host='192.168.1.5',user='root',passwd='Killer51$$',db='idea')
        conn.set_charset('utf8')
        cur=conn.cursor()
        cur.execute('set names utf8;')
        cur.execute('set character set utf8;')
        cur.execute('set character_set_connection=utf8;')
        sql="select count(0) from t_baike where title='"+title+"'"
        cur.execute(sql)
        if cur.fetchone()[0]==0:
            return False
        return True
    except:
        return True

def testSaveBaike():
    url='http://baike.baidu.com/item/%E7%94%B5%E7%BC%86'
    bsObj=getItemInBaikeByUrl(url)
    if bsObj!=None:
        item_data=getChildViews(bsObj,url)
        saveBaikeItem(item_data)


def beginScrapy(rootUrl):
    print('---------------begin scrapy url:' + rootUrl+'-----------------------------')
    bsObj=getItemInBaikeByUrl(rootUrl)
    sleep(10)
    if bsObj==None:
        return

    item_data=getChildViews(bsObj,rootUrl)
    print('------------------------data is --------------------------------')
    print(item_data)
    if item_data==None:
        return
    id=saveBaikeItem(item_data)
    if id==None:
        return
    #for child in item_data["child_views"]:
     #   if isTitleScrapyed(child["title"])==False:
      #      beginScrapy('http://baike.baidu.com'+child["href"])

if __name__=='__main__':
    beginScrapy("http://baike.baidu.com/item/%E7%94%B5%E7%BC%86")