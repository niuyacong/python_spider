""" 
urllib:python内置http请求库
urllib.request    请求模块
urllib.error       异常处理模块
urllib.parse       url解析模块
urllib.robotparser robots.txt解析模块
"""

# urllib.request
# urllib.request.urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,*, cafile=None, capath=None, cadefault=False, context=None);

import urllib.request

response=urllib.request.urlopen("http://www.baidu.com");

with urllib.request.urlopen("http://www.baidu.com") as response:
    pass;

html=response.read().decode('utf-8') # response.read()返回的是bytes,需要转换成utf8

# urllib.parse
import urllib.parse

data=bytes(urllib.parse.urlencode({"world":"hello"}),encoding="utf8")

response=urllib.request.urlopen("http://httpbin.org/post",data=data)

#header
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers={'User_Agent':user_agent,'Host':'httpbin.org'}

# method 1:
resp=urllib.request.Request(url="http://httpbin.org/post",data=data,headers=headers,method="POST")
# method="POST" post必须大写.

# method 2:
resp.add_header('User_Agent',user_agent);

response=urllib.request.urlopen(resp)
res=response.read()

# urllib.error

from   urllib.error import HTTPError,URLError
 
import socket

try:
    response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
except HTTPError as e: #HTTPError 继承了URLError,捕获异常时,应先捕获HTTPError,否则报错
    pass
except URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("time out ")
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
else:
    print('successful')

# 响应

# 状态码 响应头

response = urllib.request.urlopen("https://www.python.org");

print(response.status);                 # 200
print(response.getheaders())            # [('Server', 'nginx'), ('Content-Type', 'text/html; charset=utf-8'), .....
print(response.getheader('Server'))     # nginx


# Handler

# urllib.request.ProxyHandler

proxy_handler=urllib.request.ProxyHandler({
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
})

opener=urllib.request.build_opener(proxy_handler)

try:
    opener.open("http://www.baidu.com")
    response.read()
except:
    pass

# Cookie

import http.cookiejar

cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open("http://www.baidu.com")
for item in cookie:
    print(item.name+"="+item.value)
# BAIDUID=F152FBE58E79A78CCCABB6D2E615829E:FG=1
# BIDUPSID=F152FBE58E79A78CCCABB6D2E615829E
# H_PS_PSSID=1466_21081_18560_26350_26433_22157
# PSTM=1531279918
# BDSVRTM=0
# BD_HOME=0

# 保存cookie
filename='cookie.txt'
cookie=http.cookiejar.MozillaCookieJar(filename)
# cookie=http.cookiejar.LWPCookieJar(filename)
# cookie.load(filename,ignore_discard=True,ignore_expires=True) 加载cookie文件
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)


# urllib.parse.urlparse

# 语法：urllib.parse.urlparse(url, scheme='', allow_fragments=True)

from urllib.parse import urlparse

""" 
scheme:如果没有scheme，则使用默认值
allow_fragments:false
将#本身及后面元素添加到path或query
"""
result=urlparse("http://www.baidu.com/index.html;user?id=5#comment",scheme="https",allow_fragments=False)


print(type(result),result)
# <class 'urllib.parse.ParseResult'> ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')


# urllib.parse.urlunparse

from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','id=5','comment']

print(urlunparse(data))
# http://www.baidu.com/index.html;user?id=5#comment

# urllib.parse.urljoin 合并请求路径

# urllib.parse.urlencode

from urllib.parse import urlencode

params={
    'name':'c',
    'age':10
}
url="http://www.baidu.com?"+urlencode(params)
print(url)
# http://www.baidu.com?name=c&age=10