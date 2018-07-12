""" 
beautifulsoup 依赖于lxml,网页解析库,支持多种解析器
"""

html_doc ='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p>test</p>
<p class="story" id="test">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
'''
# 使用BeautifulSoup解析这段代码,能够得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出:
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_doc,"html.parser")
html=soup.prettify()# 得到完整的代码

# 选择标签 返回第一个匹配元素
print(soup.title)      # <title>The Dormouse's story</title>
print(type(soup.title))# <class 'bs4.element.Tag'>
print(soup.p)          # <p class="title"><b>The Dormouse's story</b></p>
print(soup.head)       # <head><title>The Dormouse's story</title></head>

# 获取标签名称
print(soup.title.name) # title
print(soup.p.name)     # p

# 获取属性
print(soup.p.attrs['class'])    # ['title']
print(soup.p['class'])          # ['title']


# 获取标签内容
print(soup.p.string)    # The Dormouse's story

# 嵌套选择
print(soup.head.title.string)   # The Dormouse's story

# 子节点和子孙节点

# 获取子节点
print(soup.p.contents)  # [<b>The Dormouse's story</b>]
print(soup.p.children)    # <list_iterator object at 0x0000000001E63470>
for i,child in enumerate(soup.p.children):
    print(i,child)      # 0 <b>The Dormouse's story</b>

# 获取子孙(子节点和子孙节点)节点
print(soup.head.descendants) # <generator object descendants at 0x00000000025619E8>
for i,child in enumerate(soup.head.descendants):
    print(i,child)

# 获取父节点
print(soup.title.parent)    # <head><title>The Dormouse's story</title></head>

# 获取祖先(父节点一直到根节点)节点
print(soup.title.parents)         # <generator object parents at 0x00000000025719E8>
for i,child in enumerate(soup.title.parents):
    print(i,child)
print(list(enumerate(soup.title.parents)))


# 获取兄弟节点
# 获取前面的兄弟节点
print(soup.p.previous_siblings) # <generator object previous_siblings at 0x00000000025819E8>
print(soup.p.next_siblings)     # <generator object next_siblings at 0x00000000025819E8>
print(list(enumerate(soup.p.previous_siblings)))
print(list(enumerate(soup.p.next_siblings)))

# 标准选择器
# 语法：find_all(name,attrs,recusive,text,**kw)
print("findall")
print(soup.find_all("p"))
print("findall0")
print(soup.find_all("p")[0])

for p in soup.find_all("p"):
    print(p.find_all("a"))

# attrs（根据标签属性）
# 以下输出内容是完全一样的，但是class 是关键字，需加下划线
print('attrs')
print(soup.find_all(attrs={'class','story'}))
print(soup.find_all(id='test'))
print(soup.find_all(class_='story'))

# text 根据标签内容
print('text')
print(soup.find_all(text='test'))   # ['test'] 返回的还是标签内容

# find_all(name,attrs,recusive,text,**kw) 返回所有匹配结果
# find(name,attrs,recusive,text,**kw) 返回匹配的第一个元素

# 返回父节点
# soup.find_parent() soup.find_parents()

# 返回后面的兄弟节点
# soup.find_next_sibling() soup.find_next_siblings()

# 返回前面的兄弟节点
# soup.find_previous_sibling() soup.find_previous_siblings()

# 返回节点后匹配的节点
# soup.find_all_next() soup.find_all()

# 返回节点前匹配的节点
# soup.find_all_previous() soup.find_previous()

# css选择器 select()
soup.select("#test")
soup.select(".title")
soup.select("p")[0]
for s in soup.select("p"):
    print(s.select("a"))
    for a in s.select("a"):
        print(a.get_text()) # 获取文本值
