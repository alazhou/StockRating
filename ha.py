#!/home/shijiezhou/anaconda3/bin/python

#local py class
import GetStockList
#from GetStockList import list_host,list_headers
from GetStockList import QuoteData
from GetStockList import StockDetials
from GetStockList import PutAvaiStock
import GetIndustryList
from GetIndustryList import GetIndustryList
#local lib
import urllib.request,urllib.error
import urllib.parse
import requests
import sys
from urllib import request
import json
import pandas as pd
import time


page = '1'
num = '30'

# address link to "Get Stock list by ttm, pb, industry..."
host=['https://xueqiu.com/service/v5/stock/screener/quote/list?page=','','&size=30&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1576554043886']
host_ttm = ['https://xueqiu.com/service/v5/stock/screener/quote/list?page=','','&size=30&order=asc&orderby=pe_ttm&order_by=pe_ttm&market=CN&type=sh_sz&_=1576832412092']
host_industry = ['https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=45&order=desc&order_by=percent&exchange=CN&market=CN&ind_code=','','&_=1577068447561']

list_headers={
        "Host":" xueqiu.com",
        "Connection":" keep-alive",
        "Accept":" */*",
        "Origin":" https://xueqiu.com",
        "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
        "Sec-Fetch-Site":" same-origin",
        "Sec-Fetch-Mode":" cors",
        "Referer":" https://xueqiu.com/hq",
        "cache-control": "no-cache",
        #"Accept-Encoding":" gzip, deflate, br",
        "Accept-Language":" en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cookie": "aliyungf_tc=AQAAAHw7kQCFSAgAflEmapYQ5Vs5W/Ik; acw_tc=2760820715765537105575976e81baac21c8193138bbfa3d0eac9e7cb746f8; xq_a_token=c9d3b00a3bd89b210c0024ce7a2e049f437d4df3; xq_r_token=8712d4cae3deaa2f3a3d130127db7a20adc86fb2; u=681576553711126; s=c211pd034m; device_id=24700f9f1986800ab4fcc880530dd0ed; Hm_lvt_1db88642e346389874251b5a1eded6e3=1576553713; __utma=1.1153413314.1576553713.1576553713.1576553713.1; __utmc=1; __utmz=1.1576553713.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1576554044; __utmb=1.3.10.1576553713"
        }
print(sys.argv[1])
page = sys.argv[1]
if len(sys.argv[1]) > 3:
    host_addr = host_industry
#elif len(sys.argv[1]) == 1:
#    host_addr = host_ttm
else:
    host_addr = host_ttm

fp = sys.argv[1]
gil = GetIndustryList(fp)
industryDict = gil.toDict()
#print(industryDict)

print(len(sys.argv))

if len(sys.argv) > 2:
    pb_bar = float(sys.argv[2])
else:
    pb_bar = 1.7

if len(sys.argv) > 3:
    pe_bar = float(sys.argv[3])
else:
    pe_bar = 17.0
	
lst_stock = []
indStock = {}
gs = GetStockList.GetStockList(host_addr,headers=list_headers)
for (v,k) in industryDict.items():
    page = k
    df_stock = pd.DataFrame( gs.toListByPage(host_addr,page))
    seq = df_stock['symbol'].tolist()
    indStock[v] = seq 
    lst_stock = lst_stock+seq
print(indStock.keys())

print('\033[1;35;5;40m')
print("请输入行业板块...")
print('\033[0m')

validinput = False
while validinput == False:
    inputind = input("")
    if inputind in indStock:
        lst_stock = indStock[inputind]
        validinput = True
    else:
        validinput = False
        print('\033[1;35;5;40m')
        print("没有输入板块,重新请输入行业板块...")
        print('\033[0m')

print(lst_stock)


# Address link to "Get stock detail infomation, like pb ,pe_lyr, pe_forecast..."
#host="http://hq.sinajs.cn/list="
#host="http://nuff.eastmoney.com/EM_Finance2015TradeInterface/JS.ashx?id="
#url = host + 'sh600006'
#host_xq = host_lst[0]+stock+host_lst[2]
#host_xq="https://stock.xueqiu.com/v5/stock/quote.json?symbol="+stock+"&extend=detail"

host_lst = ['https://stock.xueqiu.com/v5/stock/quote.json?symbol=','','&extend=detail']
xq_headers={
        "Host":" stock.xueqiu.com",
        "Connection":" keep-alive",
        "Accept":" */*",
        "Origin":" https://xueqiu.com",
        "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "Sec-Fetch-Site":" same-site",
        "Sec-Fetch-Mode":" cors",
        "Referer":" https://xueqiu.com/S/SZ000001",
        #"Accept-Encoding":" gzip, deflate, br",
        "Accept-Language":" en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cookie":" Hm_lvt_1db88642e346389874251b5a1eded6e3=1573699321; xq_a_token=c9d3b00a3bd89b210c0024ce7a2e049f437d4df3; xqat=c9d3b00a3bd89b210c0024ce7a2e049f437d4df3; xq_r_token=8712d4cae3deaa2f3a3d130127db7a20adc86fb2; u=491575870345254; device_id=24700f9f1986800ab4fcc880530dd0ed; s=cv110u98p5; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1576141038"
        }


dtls = {'symbol': 'SZ300518', 'code': '300518', 'high52w': 33.4732, 'avg_price': 28.65, 'delayed': 0, 'type': 11, 'percent': 10.0, 'tick_size': 0.01, 'float_shares': 61968106, 'limit_down': 24.02, 'amplitude': 9.78, 'current': 29.36, 'high': 29.36, 'current_year_percent': 26.65, 'float_market_capital': 1819383592.0, 'issue_date': 1466697600000, 'low': 26.75, 'sub_type': '3', 'market_capital': 2740462400.0, 'dividend': 0.02, 'dividend_yield': 0.068, 'currency': 'CNY', 'lot_size': 100, 'lock_set': None, 'navps': 11.92, 'profit': 10159391.88, 'timestamp': 1576825443000, 'pe_lyr': 269.747, 'amount': 107655152.21, 'chg': 2.67, 'eps': 0.238, 'last_close': 26.69, 'profit_four': 22780605.61, 'volume': 3758096, 'volume_ratio': 2.22, 'pb': 2.463, 'profit_forecast': 20849765.0, 'limit_up': 29.36, 'turnover_rate': 6.06, 'low52w': 18.2054, 'name': '盛讯达', 'pe_ttm': 120.298, 'exchange': 'SZ', 'pe_forecast': 131.439, 'time': 1576825443000, 'total_shares': 93340000, 'open': 26.76, 'status': 1}

final_list = [dtls]
score_list = [0]
sd = StockDetials(host_lst,req_headers=xq_headers)
#for i in  range(len(lst_stock)):
#    sd.PrintStock(sd.GetStock(host_lst,lst_stock[i]))
#    time.sleep(1)

pas = PutAvaiStock(dtls)
for i in range(len(lst_stock)):
    dtls = sd.GetStock(host_lst,lst_stock[i])
    pas.__init__(dtls)
    if pas.toFilter(pb_bar,pe_bar) == True:
        final_list.append(dtls)
        score_list.append(pas.ScoreRate())


#print(final_list[1:])
for i in range(len(final_list)-1):
    sd.PrintStock(final_list[i+1])
    print('\033[1;31;40m')
    print(score_list[i+1])
    print('\033[0m')



#print(sd.GetStock(host_lst,lst_stock[1]))

#req = urllib.request.Request(host,headers=headers)
#req = request.Request(host_xq,headers=headers)
#print(req)
#res_data = request.urlopen(req)
#print(res_data)
#cont = res_data.read()
#print(cont)
#data =  bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
#res_data = urllib.request.urlopen(url,data=data)
#res_data = urllib.request.urlopen(req)
#print(res_data.read().decode('utf-8'))
#jRes = res_data.read().decode('utf-8')
#sData = json.loads(jRes)
#quota = sData.pop('data')
#quota = quota.pop('quote')
#print(stock,':',quota['name'])
#for (k,v) in quota.items():
#    if k == 'pb' or k == 'pe_ttm' or k == 'pe_forecast' or k == 'pe_lyr':
#        print("[{: ^15}]:".format(k),v)
        #print("[%s]:".format(20)%k,v)
       # print("[","%s".ljust(key)% k,"]:","%15.3f".ljust(5)% v)
#    if k == 'current' or k == 'low52w' or k == 'high52w':
#        print("[{: ^15}]:".format(k),v)





#print(quota.keys())
#print(quota['name'],quota['pb'],quota['pe_ttm'],quota['pe_lyr'],quota['pe_forecast'])

#print(res_data.read())
#res_1 = res_data.read()

#print(res_1.text.split(',')[0][13])

#print(sys.argv[0])
#print(sys.argv[1])

#code = sys.argv[1]
#slice_num = 13
#value_num = 1
#url = host + code
#r = requests.get("http://nuff.eastmoney.com/EM_Finance2015TradeInterface/JS.ashx?id=" % (code,))
#r = requests.get(url)
# 爬取新浪股票 API                
#res = r.text.split(',')
#print(res)
#if len(res) > 1:
#   name, now = r.text.split(',')[0][slice_num:], r.text.split(',')[value_num]

#print(name)
#print(now)

