from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def get_secrets():
    return ("********","********")

def login_weibo():
    secrets=get_secrets()

    url="https://login.sina.com.cn/signup/signin.php"#登录界面(不需要验证码)
    # driver=webdriver.PhantomJS()
    driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")#使用chrome做浏览器  不然 下拉到底部的js代码无效
    driver.get(url)

    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,".form_list")))
    print("page loaded...")
    login_form=driver.find_element_by_css_selector(".form_list")

    txt_username=login_form.find_element_by_css_selector("input[name='username']")
    txt_pwd=login_form.find_element_by_css_selector("input[type='password'][name='password']")
    txt_username.send_keys(secrets[0])
    txt_pwd.send_keys(secrets[1])

    btn_login=login_form.find_element_by_css_selector("input[type='submit']")
    btn_login.click()
    sleep(10)
    print("login.....")
    print(driver.current_url)
    print(driver.get_cookies())
    return driver

def get_weibo_of_user(userId):
    driver=login_weibo()
    print('login successfully.....')
    page_count=None
    page_scrapied=1
    while True:
        if page_count!=None:
            if page_scrapied>page_count:
                break
        url="http://weibo.com/{0}?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page={1}".format(userId,page_scrapied)
        print(url)
        driver.get(url)
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.WB_feed.WB_feed_v3.WB_feed_v4")))
        js="window.scrollTo(0,document.body.scrollHeight);" 
        driver.execute_script(js)
        sleep(10)
        r=driver.execute_script("return document.body.scrollHeight;")
        print(r)
        driver.execute_script(js)
        sleep(10)
        r=driver.execute_script("return document.body.scrollHeight;")
        print(r) 

        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.W_pages")))
        if page_count==None:
            page_ul=driver.find_elements_by_css_selector("div.layer_menu_list.W_scroll ul li")[0]
            page_max_a=page_ul.find_element_by_css_selector("a").get_attribute("href")
            idx=page_max_a.find("page=")
            page_text=page_max_a[idx+5:]
            if page_text.find("#")>-1:
                idx=page_text.find("#")
                page_count=int(page_text[:idx])
            print(page_count)

        # print(driver.page_source)
        details=driver.find_elements_by_css_selector("div.WB_detail")
        print(len(details))
        all_texts=[]
        for detail in details:
            weibo_time_a=detail.find_element_by_css_selector("div.WB_from.S_txt2 a:first-child")
            weibo_content=detail.find_element_by_css_selector("div.WB_text.W_f14")
            all_texts.append((weibo_time_a.get_attribute("title"),weibo_time_a.get_attribute("date"), weibo_content.text))
        save_texts(all_texts,userId)
        page_scrapied+=1
        sleep(30)
    driver.quit()
    print('----finish scrapying {0}'.format(userId))

def save_texts(texts,userId):
    inf=open("../data/{0}.txt".format(userId),"a",encoding='utf-8')
    for t in texts:
        inf.write(t[0]+"\t"+t[1]+"\n")
        inf.write(t[2]+"\n")
    inf.close()
    print('---save texts successfully')

if __name__=="__main__":
    get_weibo_of_user("gaoxiaosong")