#参考 https://www.cnblogs.com/LinTeX9527/p/6181523.html
import requests
import re
from selenium import webdriver
from threading import Timer
import datetime

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
    r=[]
    res=re.compile('bosszone="SY_Mainnews"(.*?)class="ad-newslist-btm"',re.S)
    result=re.findall(res,html)
    for rxt in result:
        result=re.findall('<li>(.*?)</li>',rxt)
        for txt in result:
            result=re.findall('<a target="_blank" href="(.*?)" class=".*?>(.*?)</a>',txt,re.S)
            r.append(result)
        return r
    
    

def print_txt(res):
    with open('2.txt','a',encoding='utf-8') as f:
        f.write("--开始任务--时间："+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+"\n")
        for item in res:
            for i in range(len(item)):
                f.write("链接："+item[i][0]+" \t\t"+"标题："+item[i][1]+"\n")
                
            # print("名称："+item[0]+" "+item[1].strip()+" "+item[2]+" "+"评分："+item[3]+" "+item[4])
    

def time():
    html=openUrl('http://sports.qq.com/nba/?ptag=360.onebox.schedule.nba')
    txt=regule(html)
    print_txt(txt)
    
def sta():
    t = Timer(600, sta)
    t.start()
    time()
 


if __name__=="__main__":
    sta()
