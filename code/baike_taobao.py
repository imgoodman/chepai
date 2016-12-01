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

def getChildViews(bsObj):
    item_data={}
    #main content
    #child views
    main_content=bsObj.findAll("div",{"class":"main-content"})[0]

    title=main_content.findAll("dd",{"class":"lemmaWgt-lemmaTitle-title"})[0].h1.get_text()
    item_data["title"]=title

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



if __name__=='__main__':
    bsObj=getItemInBaikeByUrl()
    if bsObj!=None:
        getChildViews(bsObj)