""" 
selenium 爬取淘宝美食
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
from pyquery import PyQuery as pq
import pymongo
from selenium_example_config import *

client= pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

browser=webdriver.PhantomJS()
wait=WebDriverWait(browser, 10)
browser.set_window_size(1920, 1080)  # choose a resolution big enough,PhantomJS 需设置

def search():
    try:
        browser.get("https://www.taobao.com/")
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
        submit= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-search")))
        input.send_keys("美食")
        submit.click()
        total=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager>div>div>div>div.total")))
        return total.text
    except TimeoutError:
        search()

def page_detail(num): 
    try:
        time.sleep(2)
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
        submit= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))
        input.send_keys(num)
        submit.click()
        return browser.page_source
    except TimeoutError:
        page_detail(num)


def get_product(num,html):
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".J_MouserOnverReq")))
    doc=pq(html)
    result=doc(".J_MouserOnverReq").items()
    for item in result:
        rs= {
            'index':num,
            'title':item.find(".title").text(),
            'img':item.find("img").attr("src"),
            'price':item.find('.price').text(),
            'nums':item.find(".deal-cnt").text()[:-3]
        }
        db[MONGO_TABLE].insert(rs)
        # return rs
def main():
    total=search()
    num=re.compile('(\d+)').search(total).group(1)
    for nums in range(1,2):# int(num)+1  前十页
        html=page_detail(nums)
        if html is not None:
            get_product(nums,html)


if __name__=="__main__":
    main()