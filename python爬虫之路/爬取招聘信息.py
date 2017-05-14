import requests
from  bs4 import  BeautifulSoup
import xlwt
import  re
import time
import threading
javaList=[]

Default_Header={
    "Connection":"keep-alive",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cookie":"user_trace_token=20170215045723-63f8410ada254f6caf11e7c69c8276e6; LGUID=20170215045724-2f66b2b4-f2f8-11e6-afcd-525400f775ce; JSESSIONID=ABAAABAAAFCAAEGC96F4E63E55C616F112F5C847013B54A; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00fATEwT0o_4m0FNkUsKWNk9u000002iV8H300000Uo90RH.THL0oUhY1x60UWdBmy-bIy9EUyNxTAT0T1dbPynzrjKWmW0snjIbnH9h0ZRqwWDYnjnvwWwDPW6dfYf1fHP7wRwjfHDdnHDknWFan100mHdL5iuVmv-b5Hc4PjfLPH6YnWchTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8UA7MULR8mvqVQ1qdIAdxTvqdThP-5ydxmvuxmLKYgvF9pywdgLKW0APzm1YYnjnL%26tpl%3Dtpl_10085_14394_1%26l%3D1052356004%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E8%252581%25258C%2525E4%2525B8%25259A%2525E6%25259C%2525BA%2526xp%253Did%28%252522m4e160542%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D250%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1606; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_baidu_pc; _putrc=2B083DB5D506943C; login=true; unick=%E8%AE%A1%E6%97%BA%E6%97%BA; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=14; TG-TRACK-CODE=index_navigation; SEARCH_ID=006a8602040f40b1abf1f8a7c3f7ff84; index_location_city=%E6%88%90%E9%83%BD; _gid=GA1.2.587681591.1494767492; _ga=GA1.2.1816019904.1487105842; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1494762084,1494767462; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1494767492; LGSID=20170514211102-c7bf9d60-38a6-11e7-aec8-525400f775ce; LGRID=20170514211132-d9aa4329-38a6-11e7-bf82-5254005c3644",    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

class getLagouNet(threading.Thread):
    def __init__(self,args=()):
        super(getLagouNet,self,).__init__(args=())
        self.index=1 #记录列
        self.js=[]
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.list = ['地址', '发布时间', '公司名称', '薪资', '经验', '公司性质']
        self.sheet = self.workbook.add_sheet('招聘信息', cell_overwrite_ok=True)
        self.request=requests.session()
        self.url="https://www.lagou.com/zhaopin/Java/{}/?filterOption={}"
        #初始化头部信息
        self.request.headers.update(Default_Header)
    def run(self):
        print("线程%s开始下载"%self.getName())
        self.bankDocument(self.url.format(self._args(0), self._args(0)))

    def paqupages(self,count,url):
        for i in range(1,count):
            getLagouNet(args=(i,i)).start()

    def bankDocument(self,url):
        q=self.request.get(url)
        document=BeautifulSoup(q.content,"lxml")
        print("-----开始下载数据------")
        span= document.find_all('div',{'class':'list_item_top'})
        # find_all()
        # 方法搜索当前tag的所有tag子节点, 并判断是否符合过滤器的条件.这里有几个例子:
        # beautifusoup和tag 都是可以用.语法的
        for i in span:

            js.append(i.em.string)
            js.append(i.find('span',{"class":"format-time"}).string)
            js.append(i.find('a',href=re.compile("https://www.lagou.com/gongsi")).string)
            js.append(i.find('a',href=re.compile("https://www.lagou.com/gongsi")).string)
            js.append(i.find('span',{"class":"money"}).string)
            js.append(i.find('div',{"class":"li_b_l"}).contents[4])
            js.append(i.find('div',{"class":"industry"}).string.strip())
    def writeJson(self):
        for k in range(0, len(self.list)):
            self.sheet.write(self.index, k, js[k])
        self.index = self.index + 1

    def writeTitle(self):
        for i in range(0,len(self.list)):
            self.sheet.write(0,i,self.list[i])
    def close(self):
        self.workbook.save('招聘信息.xls')

begin=time.time()
base_url="https://www.lagou.com/zhaopin/Java/{}/?filterOption={}"
lagou =getLagouNet()
lagou.writeTitle()
lagou.paqupages(30,base_url)
lagou.close()
end=time.time()
print("消耗的时间是%s秒"%str(end-begin))