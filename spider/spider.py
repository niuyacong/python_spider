
from urllib import request
import re
''' 
beautfulshp
scrapy
'''
class Spider():
    url="https://www.panda.tv/cate/lol"
    root_partern='<div class="video-info">([\s\S]*?)</div>'
    name_parttern='</i>([\s\S]*?)</span>'
    num_parttern='<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):#__私有方法
       r=request.urlopen(Spider.url);
       htmls=r.read();
       #字节
       htmls=str(htmls,encoding="utf-8")
       return htmls

    def __analysis(self,htmls):
        root_html=re.findall(Spider.root_partern,htmls)
        findresult=[]
        for html in root_html:
            name=re.findall(Spider.name_parttern,html)
            num=re.findall(Spider.num_parttern,html)
            result={'name':name,'num':num}
            findresult.append(result)
        return findresult

    def __refine(self,anchors):
        l=lambda x:{'name':x['name'][0].strip(),'num':x['num'][0]}
        return map(l,anchors)


    def __sort(self,anchors):
        anchors=sorted(anchors,key=self.__sort_by,reverse=True)
        return anchors

    def __sort_by(self,anchors):
        num=re.findall('\d*',anchors['num'])
        number=float(num[0])
        if '万' in anchors['num']:
            number*=10000
        return number

    def __show(self,anchors):
        for rank in range(0,len(anchors)):
            print ('rank    '+str(rank+1)+'  '+anchors[rank]['name']+':'+anchors[rank]['num'])
            # print(x['name']+'----------'+x['num'])

    def go(self):
       htmls= self.__fetch_content()
       htmls=self.__analysis(htmls)
       anchors=self.__refine(htmls)
       anchors=self.__sort(list(anchors))
       self.__show(anchors)


s=Spider()
s.go()