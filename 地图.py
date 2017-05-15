import json
from echarts import Geo, Echart,Map
f= open('C:/Users/jiww/Downloads/china.json',encoding='utf8')
setting = json.load(f)
chart = Echart('CHINA', axis=False) # 不使用axis选项
chart.use(Geo({'map':'china'}))
chart.plot()
