""" 
正则表达式
1、[]只要包含元类中的字符，则返回  [^]不包含
2、概括字符集[0-9]、[a-z] 单词字符\w 非单词字符\W  非数字字符\D  数字字符\d  空白字符\s 非空白字符\S
    . 匹配除换行符之外的所有字符
3、数量词 []{n} 将前面的字符匹配多少次  []{3,6} 3到6个  正则倾向于贪婪匹配，非贪婪匹配[]{}?
    以下数量匹配只匹配相邻字符的数量，且统计字符的总数
    python*  n出现0次或多次  pytho  pythonn 都满足
    * 匹配0次或无限多次
    + 匹配1次或无限多次
    ？匹配0次或1次
4、边界匹配
    ^ 从匹配字符的开头匹配
    $ 从匹配字符的结尾匹配
5、组  []{} 匹配字符几次  (){}匹配组几次
6、匹配模式 第三个参数的位置
    re.I  不区分大小写
    re.S    回车
7、函数
    re.sub(正则,函数,字符串); 函数取值value.group(),取字符所在位置 value.span()
     
    字符串.replace()
    re.match()从字符串开头开始匹配，不匹配返回None,返回第一个匹配到的字符
    re.search()返回第一个匹配到的字符
    返回需匹配的字符需加（）
    group(0) 返回整个字符串  group(1,2,3)返回匹配元组 groups()返回所有匹配元组
    re.findall()返回所有匹配元组 

    re.compile 复用
"""
import requests
import re

response=requests.get("https://book.douban.com/")

# print(response.text)


# pattern=re.compile('<div class="title">.*?<a.*?href="(.*?)".*?</div>.*?<div class="author">([\s\S]*?)</div>',re.S)
res=re.findall('<div class="title">.*?<a.*?href="(.*?)".*?</div>.*?<div class="author">([\s\S]*?)</div>',response.text,re.S)
for key,val in res:
    print(re.sub('\n','',key),re.sub('\n','',val)),
# print(res)
print(1)

