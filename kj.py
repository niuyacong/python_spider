""" 
1、Pyspider
    cmd : pip install Pyspider
          Pyspider all
    浏览器输入 localhost:5000

2、scarpy
    安装依赖库：
    pip install wheel
    pip install lxml  也可以下载lxml whl文件  运行这个文件
    pip install PyOpenSSL  步骤也可同上
    Twisted  https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted  下载whl文件
    Pywin32  pip install pywin32
    Scrapy   pip install scrapy
 

 scrapy 使用：
# 创建了一个名为test的项目
 scrapy startproject test 
#进入项目
 cd test
# 创建一个模块
 scrapy genspider  quotes quotes.toscrape.com   
"""