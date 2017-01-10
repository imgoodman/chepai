#!/usr/bin/python  
#-*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import pymysql



def begin_search(search_id,search_name=None,search_publish_code=None,search_keyword=None):
    if search_name==None and search_publish_code==None and search_keyword==None:
        return
    print('search condition is:name="{1};code={2};keyword={3} in id={0}"'.format(search_id,search_name,search_publish_code,search_keyword))
    #open browser
    driver = webdriver.PhantomJS()
    url='http://www.pss-system.gov.cn/sipopublicsearch/patentsearch/tableSearch-showTableSearchIndex.shtml'
    driver.get(url)

    #检查页面是否加载完成
    # try:
    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'btn-search')))

    #page loads successfully
    if search_name!=None:
        input_name=driver.find_element_by_id('tableSearchItemIdIVDB077')
        input_name.send_keys(search_name)

    if search_publish_code!=None:
        input_publish_code=driver.find_element_by_id('tableSearchItemIdIVDB075')
        input_publish_code.send_keys(search_publish_code)
    
    if search_keyword!=None:
        input_keyword=driver.find_element_by_id('tableSearchItemIdIVDB086')
        input_keyword.send_keys(search_keyword)

    btn_generate= driver.find_element_by_class_name('btn-generate')
    btn_generate.click()

    time.sleep(1)
    #click search_id
    btn_search = driver.find_elements_by_class_name('btn-search')
    btn_search[1].click()

    #wait search_result show
    WebDriverWait(driver,20).until_not(EC.presence_of_element_located((By.CLASS_NAME,'blockUI')))

    time.sleep(5)

    #total result count
    result_totalCount=int(driver.find_element_by_id('result_totalCount').get_attribute('value'))

    if result_totalCount==0:
        finish_search(search_id)
        print('no result in this search {0}'.format(search_id))
        return
    
    patents=[]

    list_container=driver.find_elements_by_css_selector('.list-container ul li.patent div.item')
    patents=get_patent_info_of_container(list_container)
    print('the patents of the first page is:')
    for p in patents:
        print(p['id'])

    #check if needs to paging
    if result_totalCount>12:
        print('there are more than one page results, and begin paging')
        #a lot of pages
        total_pages=int(result_totalCount/12)+(0 if result_totalCount%12==0 else 1)-1
        for i in range(total_pages):
            print('begin paging {0}'.format(i+2))
            #next page click
            btn_next_page = driver.find_elements_by_css_selector('.page_top a')[2]
            if btn_next_page.get_attribute('href')!='#':
                btn_next_page.click()

                #wait for result show
                WebDriverWait(driver,20).until_not(EC.presence_of_element_located((By.CLASS_NAME,'blockUI')))

                time.sleep(5)

                list_container=driver.find_elements_by_css_selector('.list-container ul li.patent div.item')
                new_patents=get_patent_info_of_container(list_container)
                print("new patents")
                for p in new_patents:
                    print(p['id'])
                patents.extend(new_patents)
            
            #if count of parents are more than 200, then save them to db, and continue to scrapy
            if len(patents)>100:
                save_patents_to_db(patents,search_id)
                patents=[]
    else:
        save_patents_to_db(patents,search_id)
    finish_search(search_id)
    driver.quit()
    # except Exception as e:
    #     print('can not load {0} in 10 seconds, and exit the search'.format(url))
    #     print(e)
    #     return



def get_patent_info_of_container(list_container):
    patents=[]
    for item in list_container:
        patent_info={}
        #文献标识（不知道与下面的字段什么区别）
        vId = item.find_element_by_name('vIdHidden')
        patent_info['vId']=vId.get_attribute('value')

        #文献唯一标识
        id = item.find_element_by_name('idHidden')
        patent_info['id']=id.get_attribute('value')

        #发明名称
        title = item.find_element_by_name('titleHidden')
        patent_info['title']=title.get_attribute('value')

        #nrdAn
        nrdAn = item.find_element_by_name('nrdAnHidden')
        patent_info['nrdAn']=nrdAn.get_attribute('value')

        patents.append(patent_info)
        
    return patents


def get_detail_of_patent():
    driver = webdriver.PhantomJS()
    conn,cur=get_conn()
    while True:
        sql='select id,sid,nrdAn from t_patent where is_detail_loaded=0 order by scrapy_time asc limit 1'
        cur.execute(sql)

        if cur.rowcount==0:
            break

        row = cur.fetchone()
        url_detail = 'http://www.pss-system.gov.cn/sipopublicsearch/patentsearch/showAbstractInfo-viewAbstractInfo.shtml?nrdAn={0}&cid={1}&sid={1}&wee.bizlog.modulelevel=0201101'.format(row[2],row[1])
        
        #http://www.pss-system.gov.cn/sipopublicsearch/patentsearch/showAbstractInfo-viewAbstractInfo.shtml?nrdAn=CN201510942152&cid=CN201510942152.820160420FM&sid=CN201510942152.820160420FM&wee.bizlog.modulelevel=0201101
        #上述是详情的返回结果
        print("current record id is:{0}".format(row[0]))
        print(url_detail)
        driver.get(url_detail)
        info = driver.find_element_by_tag_name('pre')
        #print(info.text)

        json_detail=json.loads(info.text)
        time.sleep(10)
        # print('json detail:')
        # print(json_detail)
        patent_detail={}
        patent_detail['name']=json_detail['abstractInfoDTO']['tioIndex']['value']

        patent_detail['apply_code']=json_detail['abstractInfoDTO']['abstractItemList'][0]['value']
        patent_detail['apply_date']=json_detail['abstractInfoDTO']['abstractItemList'][1]['value']
        patent_detail['publish_code']=json_detail['abstractInfoDTO']['abstractItemList'][2]['value']
        patent_detail['publish_date']=json_detail['abstractInfoDTO']['abstractItemList'][3]['value']
        patent_detail['ipc_code']=json_detail['abstractInfoDTO']['abstractItemList'][4]['value']
        patent_detail['applier_name']=json_detail['abstractInfoDTO']['abstractItemList'][5]['value']
        patent_detail['inventor_name']=json_detail['abstractInfoDTO']['abstractItemList'][6]['value']
        patent_detail['priority_code']=json_detail['abstractInfoDTO']['abstractItemList'][7]['value']
        patent_detail['priority_date']=json_detail['abstractInfoDTO']['abstractItemList'][8]['value']
        
        print(len(json_detail['abstractInfoDTO']['abstractItemList']))
        if len(json_detail['abstractInfoDTO']['abstractItemList'])>9:
            patent_detail['applier_address']=json_detail['abstractInfoDTO']['abstractItemList'][9]['value']
        if len(json_detail['abstractInfoDTO']['abstractItemList'])>10:
            patent_detail['applier_zip']=json_detail['abstractInfoDTO']['abstractItemList'][10]['value']

        patent_detail['abstract']=json_detail['abstractInfoDTO']['abIndexList'][0]['value']
        patent_detail['pn']=json_detail['abstractInfoDTO']['pn']
        patent_detail['db_code']=json_detail['abstractInfoDTO']['dbCode']
        patent_detail['figure_id']=json_detail['abstractInfoDTO']['figureRid']
        # print('what we need is:')
        # print(patent_detail)

        sql="update t_patent set "
        #sql='update t_patent set name="{0}",apply_code="{1}",apply_date="{2}",publish_code="{3}",publish_date="{4}",ipc_code="{5}",applier_name="{6}",inventor_name="{7}",priority_code="{8}",priority_date="{9}",applier_address="{10}",applier_zip="{11}",abstract="{12}" where id='
        sql+=','.join([k+"='"+ patent_detail[k].replace("'","\"") +"'" for k in patent_detail if patent_detail[k]!=None])
        sql+=',is_detail_loaded=1 where id='+str(row[0])
        #print(sql)
        cur.execute(sql)
        conn.commit()
    driver.quit()
    close_conn(conn,cur)

def get_secrets():
    return None

def get_conn():
    secrets=get_secrets()
    conn=pymysql.connect(host=secrets[0],user=secrets[1],passwd=secrets[2],db=secrets[3])
    conn.set_charset('utf8')
    cur=conn.cursor()
    cur.execute('set names utf8;')
    cur.execute('set character set utf8;')
    cur.execute('set character_set_connection=utf8;')
    return (conn,cur)
def close_conn(conn,cur):
    cur.close()
    conn.close()

def finish_search(id):
    update_search_state(id,1)

def terminate_search(id):
    update_search_state(id,2)

def update_search_state(id,state):
    conn,cur=get_conn()
    sql='update t_patent_search set state={0} where id={1}'.format(state,id)
    cur.execute(sql)
    conn.commit()
    close_conn(conn,cur)

def get_search():
    conn,cur=get_conn()
    sql='select id,name,publish_code,keyword from t_patent_search where state=0 limit 1'
    cur.execute(sql)
    ret=None
    #是否有需要检索的
    if cur.rowcount>0:
        row=cur.fetchone()
        ret=(row[0],row[1],row[2],row[3])
    close_conn(conn,cur)
    return ret

def save_patents_to_db(patents,search_id):
    conn,cur=get_conn()
    for p in patents:
        sql='select count(0) from t_patent where patent_id="{0}"'.format(p['id'])
        cur.execute(sql)
        if cur.fetchone()[0]==0:
            sql='insert into t_patent (search_id,nrdAn,sid,cid,name,patent_id) values ("{0}","{1}","{2}","{2}","{3}","{2}")'.format(search_id,p['nrdAn'],p['id'],p['title'])
            print('insert {0}'.format(p['id']))
            cur.execute(sql)
        else:
            print('the patent id {0} already exists and skip'.format(p['id']))
    conn.commit()
    print('save patents {0} into database successfully'.format(len(patents)))
    close_conn(conn,cur)

if __name__=='__main__':
    ret=get_search()
    if ret!=None:
        begin_search(ret[0],ret[1],ret[2],ret[3])
    else:
        get_detail_of_patent()