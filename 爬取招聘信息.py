import requests
from  bs4 import  BeautifulSoup
import  re
import  time
import  lxml
import xlwt
import  threading

workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('招聘信息', cell_overwrite_ok=True)
list = ['地址', '发布时间', '公司名称', '薪资', '经验', '公司性质']
for i in range(0,len(list)):
    sheet.write(0,i,list[i])
workbook.save('招聘信息.xls')
Default_Header={
    "Connection":"keep-alive",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cookie":"user_trace_token=20170215045723-63f8410ada254f6caf11e7c69c8276e6; LGUID=20170215045724-2f66b2b4-f2f8-11e6-afcd-525400f775ce; JSESSIONID=ABAAABAAAFCAAEGC96F4E63E55C616F112F5C847013B54A; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00fATEwT0o_4m0FNkUsKWNk9u000002iV8H300000Uo90RH.THL0oUhY1x60UWdBmy-bIy9EUyNxTAT0T1dbPynzrjKWmW0snjIbnH9h0ZRqwWDYnjnvwWwDPW6dfYf1fHP7wRwjfHDdnHDknWFan100mHdL5iuVmv-b5Hc4PjfLPH6YnWchTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8UA7MULR8mvqVQ1qdIAdxTvqdThP-5ydxmvuxmLKYgvF9pywdgLKW0APzm1YYnjnL%26tpl%3Dtpl_10085_14394_1%26l%3D1052356004%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E8%252581%25258C%2525E4%2525B8%25259A%2525E6%25259C%2525BA%2526xp%253Did%28%252522m4e160542%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D250%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1606; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_baidu_pc; _putrc=2B083DB5D506943C; login=true; unick=%E8%AE%A1%E6%97%BA%E6%97%BA; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=14; TG-TRACK-CODE=index_navigation; SEARCH_ID=006a8602040f40b1abf1f8a7c3f7ff84; index_location_city=%E6%88%90%E9%83%BD; _gid=GA1.2.587681591.1494767492; _ga=GA1.2.1816019904.1487105842; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1494762084,1494767462; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1494767492; LGSID=20170514211102-c7bf9d60-38a6-11e7-aec8-525400f775ce; LGRID=20170514211132-d9aa4329-38a6-11e7-bf82-5254005c3644",    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
lock=threading.Lock()
request=requests.session()
request.headers.update(Default_Header)
def readAndWrite(pageindex,baseUrl,column,threadName):
        allList = []
        url=baseUrl.format(pageindex+1,pageindex+1)
        q = request.get(url)
        document = BeautifulSoup(q.content, "lxml")
        print(str(threadName)+"-----开始下载数据------")
        span = document.find_all('div', {'class': 'list_item_top'})
        try:
            for i in span:
                 js = []
                 js.append(i.em.string)
                 js.append(i.find('span', {"class": "format-time"}).string)
                 js.append(i.find('a', href=re.compile("https://www.lagou.com/gongsi")).string)
                 js.append(i.find('span', {"class": "money"}).string)
                 js.append(i.find('div', {"class": "li_b_l"}).contents[4].strip())
                 js.append(i.find('div', {"class": "industry"}).string.strip())
                 allList.append(js)
                 print(allList)
            if lock.acquire():
                columnIndex = column
                for k in range(0, len(allList)):
                    sheet.write(columnIndex, 0, allList[0][0])
                    sheet.write(columnIndex, 1, allList[0][1])
                    sheet.write(columnIndex, 2, allList[0][2])
                    sheet.write(columnIndex, 3, allList[0][3])
                    sheet.write(columnIndex, 4, allList[0][4])
                    sheet.write(columnIndex, 5, allList[0][5])
                    print("我的列是" + str(columnIndex))
                    allList.pop(0)
                    columnIndex = columnIndex + 1
        except Exception as e:
                print("异常信息"+e)
        finally:
                lock.release()
threads=[]
#每页15条数据
url="https://www.lagou.com/zhaopin/Java/{}/?filterOption={}"
#开始从第二行开始写
index=1
begin=time.time()
for i in range(30):
    thread = threading.Thread(target=readAndWrite,args=(i,url,index,"线程%s"%str(i+1)))
    index+=15
    threads.append(thread)
for i in threads:
    i.start()
for i in threads:
    i.join()
print("数据下载完成.....")
end=time.time()
print("消耗的时间%f秒"%(end-begin))
workbook.save('招聘信息.xls')