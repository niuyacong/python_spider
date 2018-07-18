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
        brower=webdriver.Chrome();
        brower.get(url)
        return brower.page_source
     except RequestException:
        print('请求索引页出错')
        return None

def parse_page_detail(html):
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].get_text()
    print(title)
    images_pattern=re.compile('JSON.parse(.*?)siblingList:',re.S)
    result=re.findall(images_pattern,html)
    
    if result:
        data=result[0].strip('\n')
        l=len(data)-7
        datas=data[1:l]
        print(datas)
        json_data=json.loads(result[0].strip('\n'))
        print(type(json_data))
        for item in json_data['sub_images']:
                print(item)


def main():
    html= get_page_index(0,'街拍')
    for url in parse_page_index(html):
        print(url)
        if url is not None:
            html=get_page_detail(url)
            parse_page_detail(html)

if __name__=="__main__":
    main()