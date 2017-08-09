#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import user_agents
import random
import time
import spidermethod
import requests
import json


debug = 0

def get_ajax(url):
    dcap = dict(DesiredCapabilities.CHROME)
    dcap["Chrome.page.settings.userAgent"] = (random.choice(user_agents.user_agent_list))
    #加上随机文件头，调用浏览器访问
    driver = webdriver.Chrome(desired_capabilities=dcap)
    #正是处理的时候，这里使用PhantomJS浏览
    driver.implicitly_wait(10)
    driver.get(url)
    page_html = BeautifulSoup(driver.page_source,'html.parser')
    #获取soup处理之后的页面代码
    driver.close()
    return page_html 


def get_page_html(url):
    dcap = dict(DesiredCapabilities.CHROME)
    dcap["Chrome.page.settings.userAgent"] = (random.choice(user_agents.user_agent_list))
    #加上随机文件头，调用浏览器访问
    driver = webdriver.Chrome(desired_capabilities=dcap)
    #正是处理的时候，这里使用PhantomJS浏览
    driver.implicitly_wait(10)
    driver.get(url) 
    #这里打开本地浏览器，调用浏览器内核访问目标网址
    
    
    target = driver.find_element_by_xpath('//*[@id="navBackToTop"]/div/span')
    driver.execute_script('arguments[0].scrollIntoView();',target)
    #driver.refresh()
    #尝试访问页面，访问失败就刷新一次

    #滚动到页面最下面
    time1 = time.time()
    i = 0
    while 1:
        time.sleep(5)
        page_source_1 = driver.page_source
        time.sleep(5)
        page_source_2 = driver.page_source
        if page_source_2 == page_source_1:
            break
    time2 = time.time()
    print int(time2-time1)
    page_html = BeautifulSoup(driver.page_source,'html.parser')
    #获取soup处理之后的页面代码
    driver.close()
    return page_html

def get_user_comments(prod):
    pro_name = prod.find(class_="a-size-medium a-color-base glimpse-product-title glimpse-flex-item").get_text().strip()

    prod_pic = prod.find(class_="a-column a-span12 a-spacing-small a-ws-span4")
    prod_pic = prod_pic.find('img')
    prod_pic = prod_pic['src']
    # print prod_pic

    try:
        pro_type = prod.find(class_="a-size-medium a-color-base glimpse-product-title glimpse-flex-item")
        pro_type = pro_type.get_text()
    except:
        pro_type = 'N/A'
    #获取评论的标题
    try:
        comment_time = prod.find(class_="a-size-base a-color-base")
        comment_time = comment_time.get_text()
    except:
        comment_time = 'N/A'
    #获取评论的时间
    try:
        stars = prod.find('i')
        stars = stars['class']
        stars = stars[-1]
        stars = filter(str.isdigit, str(stars))
    except:
        stars = 'N/A'
    #获取评论的星级
    try:
        title = prod.find(class_="a-color-base glimpse-review-title glimpse-flex-item a-text-bold")
        title = title.get_text()
    except:
        title = 'N/A'
    #获得评论标题
    try:
        content = prod.find(class_="a-color-base glimpse-review-summary glimpse-flex-item")
        content = content.get_text()
    except:
        content = 'N/A'
    #获取评论内容
    pro_page = prod.find_all(class_="a-link-normal")
    pro_page = (pro_page[1])['href']
    page_url = pro_page
    #print page_url
    #获取评论本身链接
    # print page_url
    good_page_soup = spidermethod.get_htmlsoup(page_url)
    #good_page_soup = get_ajax(page_url)
    #soup处理目标网址的html
    good_class = good_page_soup.find(class_="cBox secEyebrow")
    good_class = good_class.find('a')
    good_url = good_class['href']
    prod_asin = (good_url.split('/'))[5]
    try:
        pro_attribute = good_page_soup.find(class_="crDescription")
        pro_price = pro_attribute.find(class_="price").get_text().strip()
    except:
        pro_price = 'N/A'
    #获取产品的asin
    # if debug:
    #     print good_url
    good_soup = spidermethod.get_htmlsoup(good_url)
    #good_soup = get_ajax(good_url)
    try:
        good_type = good_soup.find(class_="a-unordered-list a-horizontal a-size-small")
        good_type = good_type.find_all('li')
        tmp = []
        for i in good_type:
            rst = (i.get_text()).strip()
            tmp.append(rst)

        good_type = ''.join(tmp)
        good_type = good_type.replace(u'\u203a',',').strip()
    except:
        good_type = 'N/A'

    result = [page_url,content,'N/A',prod_asin,pro_name,pro_price,stars,page_url,comment_time]
    #print result
    return result
    #返回一个元组

def get_result_list(name):
    url = 'https://www.amazon.com'+name.strip()
    print url


    page_html = get_page_html(url)
    username = page_html.find(class_="a-size-extra-large")
    username = username.get_text()
    user_icon = page_html.find(id="customer-profile-avatar-image")
    user_icon = user_icon.find('img')
    user_icon = user_icon['src']
    page_html = page_html.find(id="feed-content")
    prod_list = page_html.find_all(class_="a-row glimpse-card-main")
    # print get_user_comments(prod_list[0])
    
    print len(prod_list)
    print 'get_production_list_finished'
    result_list = []
    print 'try to get data'
    for prod in prod_list:
        try:
            result_list.append(get_user_comments(prod))
        except:
            continue
    # while 1:
    #     try:
    #         pool = ThreadPool(10)
    #         print 'try to get data'
    #         result_list = pool.map(get_user_comments,prod_list)
    #         break
    #     except:
    #         continue
    # pool.close()
    
    fh = open('customer_bought.txt','a')
    count= 0
    headers = ['customer_code','username','comments_code','comments_content','order_code','pro_asin','pro_name','pro_price','pro_stars','comment_link','comment_time']
    for line in result_list:
        write_in = [name.strip(),username]+ line
        rows = {}
        for name in headers:
            rows[name] = (write_in[headers.index(name)]).strip()
            
        json_content = json.dumps(rows)
        fh.write(json_content)
        count+=1
        fh.write('\n')
            #print write_in
    fh.close()
    print count

def refresh():
    fh = open('custmer.txt','r')
    site_list = fh.readlines()
    fh = open('custmer.txt','w')
    for i in site_list[1:]:
        fh.write(i)
    fh.close()

def getStatusCode(url):
    r = requests.get(url, allow_redirects = False)
    return str(r.status_code)
 
fh = open('custmer.txt','r')
custmer_list = fh.readlines()
fh.close()    

name_count = 0
for name in custmer_list:
    count = 0
    url = 'https://www.amazon.com'+name.strip()
    if getStatusCode(url) == '404':
        refresh()
        continue
    while 1:
        try:
            get_result_list(name)
        #write_result(result_list)
            break
        except:
            count = count+1
            if count == 10:
                break

    if debug:
        time.sleep(3)
        continue

    refresh()
    time.sleep(3)
    



