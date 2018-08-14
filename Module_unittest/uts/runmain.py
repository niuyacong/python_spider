""" 
执行请求的类
"""
import requests
import json
class RunMethod:
    def get_mthod(self,url,data=None,header=None):
        res=None
        if header is None:
            res=requests.get(url=url,data=data).json()
        else:
            res=requests.get(url=url,data=data,headers=header).json()
        return res
    def post_mthod(self,url,data=None,header=None):
        res=None
        if header is None:
            res=requests.post(url=url,data=data).json()
        else:
            res=requests.post(url=url,data=data,headers=header).json()
        return res
    
    def run_method(self,method,url,data=None,header=None):
        res=None
        if method=="POST":
            res=self.post_mthod(url,data,header)
        else:
            res=self.get_mthod(url,data,header)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)