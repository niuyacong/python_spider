""" 
requests
1、安装 pip3 install requests

"""

import requests

data={
    'name':'n',
    'age':10
}

# requests.get()
# requests.post()

response=requests.get("http://www.httpbin.org/get",params=data)


print(response.text)
print(response.status_code)
print(requests.status_codes==200)
print(response.cookies)
for key,value in response.cookies.items():
    pass
print(response.history)
print(response.url)
print(response.json())  # json格式

import json
print(json.loads(response.text))

# 二进制文件的解析

print(response.content)

with open('favico.ico','wb') as f:
    f.write(response.content);
    f.close()

# 添加headers
headers={'User_Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
response=requests.get("http://www.httpbin.org/get",headers=headers)

# 文件上传

files={'file':open('facico.ico','rb')}
res=requests.post('http://www.httpbin.org/post',files=files)
print(res.text)


# 会话维持

s=requests.session()
s.get("http://www.httpbin.org/get")
s.get("http://www.httpbin.org/cookie")

# 证书验证
# 错误的证书不验证

from requests.packages import urllib3

#1、
urllib3.disable_warnings()
requests.get('',verify=False)# 不验证
# 2、
requests.get('',cert=('证书','key'))


## 代理设置
proxy={
    'http':'http://127.0.0.1:9743',
    'https':'https://127.0.0.1:9743'
}
requests.get('',proxies=proxy)

# socks
# 安装： pip3 install 'requests[socks]'

# 超时设置
requests.get('',timeout=0.1)


# 认证设置

from requests.auth import HTTPBasicAuth

r=requests.get('',auth=HTTPBasicAuth('use','123'))
r=requests.get('',auth=('use','123'))


# 异常捕获
from  requests.exceptions import HTTPError,ReadTimeout

try:
    requests.get('')
except HTTPError:
    pass
except ReadTimeout:
    pass