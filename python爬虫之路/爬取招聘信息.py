import requests
from  bs4 import  BeautifulSoup
import  re
javaList=[]
Default_Header={
    "Connection":"keep-alive",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cookie":"user_trace_token=20170112125013-b5768a5dc4364d4dbaf087cc0909e96a; LGUID=20170112125013-9a9e38be-d882-11e6-8bd8-5254005c3644; index_location_city=%E6%88%90%E9%83%BD; JSESSIONID=ABAAABAAAFCAAEG381E66BE5C6D115F41B56BC352459B77; _gid=GA1.2.656262765.1494576128; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1492505916,1494576128; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1494576128; _ga=GA1.2.671273974.1484196621; LGSID=20170512160205-4a0a6be9-36e9-11e7-bce2-5254005c3644; PRE_UTM=; PRE_HOST=www.google.com.hk; PRE_SITE=https%3A%2F%2Fwww.google.com.hk%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20170512160205-4a0a6dcd-36e9-11e7-bce2-5254005c3644; TG-TRACK-CODE=index_navigation",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

class getLagouNet(object):
    def __init__(self):
        self.request=requests.session()
        #初始化头部信息
        self.request.headers.update(Default_Header)

    def bankDocument(self,url):
        q=self.request.get(url)
        document=BeautifulSoup(q.content,"lxml")
        print("-----开始下载数据------")
        span= document.find_all('div',{'class':'list_item_top'})
        # find_all()
        # 方法搜索当前tag的所有tag子节点, 并判断是否符合过滤器的条件.这里有几个例子:
        # beautifusoup和tag 都是可以用.语法的
        for i in span:
            js={}
            js['地址']=i.em.string
            js['发布时间']=i.find('span',{"class":"format-time"}).string
            js['公司名称']=i.find('a',href=re.compile("https://www.lagou.com/gongsi")).string
            js['薪资']=i.find('span',{"class":"money"}).string
            #get_text("-",strip=True)[7:]
            print(i.find('div',{"class":"li_b_l"}).next.string)

url="https://www.lagou.com/zhaopin/Java/?labelWords=label"
lagou =getLagouNet()
lagou.bankDocument(url)