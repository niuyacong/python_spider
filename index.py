''' 
需要安装的库：
1、requests re(内置库)
2、selenium pip3 install selenium
    安装完成测试：
    from selenium import webdriver
    driver=webdriver.Chrome() (启动浏览器)

    提示找不到文件，接下来下载chromedriver.exe （放入path中）
    将chromedriver.exe 文件放到 where pyhton 的文件夹下stripts文件夹下
    (保证chromedriver和chrome版本兼容)  运行
    driver.get('url');  (访问地址)
    driver.page_source  页面源代码
3、无界面的浏览器引擎 webkit (PhantomJS)
    下载（放入path中）
    from selenium import webdriver
    driver=webdriver.PhantomJS()
    driver.get('url');  (访问地址)
    driver.page_source  页面源代码

4、lxml：方便解析
    pip3 install lxml

5、beautifulsoup 依赖于lxml,网页解析库
    pip3 install beautifulsoup4
    from bs4 import BeautifulSoup

6、pyquery 网页解析库，语法和jquery一样
    pip3 install pyquery
    from pyquery import PyQuery as pq
    dic=pq('<html>hello</html>')
    result=doc('html').text()
    输出hello

7、pymysql  存储数据
    pip3 install pymysql 

    import pymysql
    connect=pymysql.connect(host='localhost',user='root',password='111111',port=3306,db='mytest')
    cursor=connect.cursor()
    cursor.execute('select id,username,password from user')
    data=cursor.fetchall()
    print(data)

8、pymongo 非关系型数据库中最像关系型数据库的 ,支持大数据量存储
    pip3 install pymongo
    import pymongo
    client=pymongo.MongoClient('localhost')
    db=client['newtestdb']
    db['table'].insert({'name':'bob'})
    db['table'].find_one({'name':'bob'})

9、reids 非关系型数据库 支持队列
    pip3 install redis
    import redis
    r=redis.Redis('localhost',6379)
    r.set('name','bob')
    r.get('name')


10、flask web服务
    pip3 install flask
    import flask

11、django web服务器框架
    pip3 install django
    import django 

12、jupyter 网页版文本编辑器 在线编辑代码 调试代码
    pip3 install jupyter
    jupyter notebook 打开网页版文本编辑器
'''

