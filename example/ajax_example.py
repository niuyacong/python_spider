''' 
今日头条  街拍

'''
import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from ajax_example_config import *
import pymongo
import os
from hashlib import md5
from multiprocessing import pool
import datetime

client= pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]

def get_page_index(offset,keywords):
    data={
        'offset':offset,
        'format':'json',
        'keyword':keywords,
        'autoload':'true',
        'count':10,
        'cur_tab':1,
        'from':'search_tab'
    }
    try:
        url="https://www.toutiao.com/search_content/?"+urlencode(data);
        headers={'User_Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def parse_page_index(html):
    data=json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
     try:
        brower=webdriver.PhantomJS();
        brower.get(url)
        return brower.page_source
     except RequestException:
        print('请求索引页出错')
        return None

def parse_page_detail(url,html):
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].get_text()
    images_pattern=re.compile('"url.*?:(.*?),',re.S)
    result=re.findall(images_pattern,html)
    tu_result=[];
    # print(result)
    date=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    for index in  range(len(result)):
        if index%4==0:
            l=len(result[index])-2
            s=result[index][2:l]
            content=down_load(s.replace("\\\/","/"))
            if content is not None:
                path=save_img(date,content)
                tu_result.append(path);
    return {
        'title':title,
        'url':url,
        'result':tu_result
    }

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储mongo成功')
        return True
    return False


def down_load(url):
    print('正在下载：'+url)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.content
        return None
    except RequestException:
        print('请求失败')
        return None
def save_img(index,content):
    print('保存图片')
    print(index)
    path='{0}/{1}'.format(os.getcwd()+"/download_pic",index)
    if not os.path.exists(path):
        os.makedirs(path)
    new = content.strip() # or new.split()[index]
    hs = md5(str(new).encode()).hexdigest()
    file_path='{0}/{1}.{2}'.format(path,hs ,'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()
        return file_path
def main(offset):
    html= get_page_index(offset,KEYWORDS)
    for url in parse_page_index(html):
        if url is not None:
            html=get_page_detail(url)
            result=parse_page_detail(url,html)
            if result:save_to_mongo(result)

if __name__=="__main__":
    groups=[x*20 for x in range(GROUP_START,GROUP_END+1)]
    pool=pool.Pool()
    pool.map(main,groups)
