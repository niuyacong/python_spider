""" 
selenium 爬取淘宝美食
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


browser=webdriver.PhantomJS()

wait=WebDriverWait(browser, 10)
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
    print(num)
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
    submit= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))
    input.send_keys(num)
    submit.click()

def main():
    total=search()
    num=re.compile('(\d+)').search(total).group(1)
    for nums in range(2,int(num)+1):
        print(nums)
        page_detail(nums)

if __name__=="__main__":
    main()