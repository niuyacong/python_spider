""" 
requests+正则 猫眼
"""
import requests
import re
from selenium import webdriver

# 获取网页内容
def openUrl(url):
    brower=webdriver.Chrome()
    try:
        brower.get(url)
        return brower.page_source
    except:
        pass
    finally:
        pass
def regule(html):
    res=re.compile('<dd>.*?<p class="name">.*?>(.*?)</a>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i>.*?<i class="fraction">(.*?)</i>',re.S)
    result=re.findall(res,html)
    return result

def print_txt(res):
    with open('biji.txt','a',encoding='utf-8') as f:
        for item in res:
            f.write("名称："+item[0]+" \t\t"+item[1].strip()+" \t\t"+item[2]+" \t\t"+"评分："+item[3]+" "+item[4]+"\n")
            # print("名称："+item[0]+" "+item[1].strip()+" "+item[2]+" "+"评分："+item[3]+" "+item[4])
    


    

html=openUrl('http://maoyan.com/board/7')
txt=regule(html)

print_txt(txt)
