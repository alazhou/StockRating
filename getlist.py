#!/home/shijiezhou/anaconda3/bin/python

import urllib.request,urllib.error
import urllib.parse
import requests
import sys
from urllib import request
import json
#import tushare as ts
#from tushare import *

#temp = ts.get_today_all()

#pb_list = temp.pb
#print(pb_list)

#print(ts.realtime_boxoffice())
page = '1'
num = '30'

#if stock[:2] == '00':
#    stock = 'SZ'+stock
#elif stock[:2] == '60':
#    stock = 'SH'+stock
#else:
#    pass

list_host = "https://xueqiu.com/service/v5/stock/screener/quote/list?page="+page+"&size="+num+"&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1576554043886"

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

#req = urllib.request.Request(host,headers=headers)
#req = request.Request(list_host,headers=headers)
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
#stock_list = quota.pop('list')

#for i in range(len(stock_list)):
#    sym = stock_list[i]
#    print(sym['symbol'],sym['name'],sym['pe_ttm'])

#print(quota.keys())
#print(quota['name'],quota['pb'],quota['pe_ttm'],quota['pe_lyr'],quota['pe_forecast'])

#print(res_data.read())
#res_1 = res_data.read()

#print(res_1.text.split(',')[0][13])


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

class QuoteData:
    def __init__(self):
        self.stockid = ''
        self.stockName = ''
        self.pe_lyr = ''
        self.pe_ttm = ''
        self.pe_forecast = ''
        self.pb= ''
        self.current = ''
        self.low52 = ''
        self.hi52 = ''

    def Print(self):
        print ("%s(%s)       %s  %s  %s %s %s %s" % (self.stockName, self.stockid, self.lastPrice, self.preClose, self.openPrice, self.lowPrice, self.highPrice, self.avgPrice))

class GetStockList:
    #list_host = ''
    #headers = {""}
    #stock_list = []
    #count = 0
    def __init__(self,list_host,headers):
        self.list_host = list_host
        self.headers = headers
        self.count = 0
    def setPage(self,page,num):
        pass
    def toListByPage(self):
        req = request.Request(self.list_host,headers = self.headers)
        res_data = request.urlopen(req)
        jRes = res_data.read().decode('utf-8')
        sData = json.loads(jRes)
        quota = sData.pop('data')
        self.count = quota.pop('count')
        stock_list = quota.pop('list')
        return stock_list
    def toNum(self):
        print("stock list have %5d stocks"%self.count)
        return self.count;
    def toPrint(self,sList):
        for i in range(len(sList)):
            sym = sList[i]
            print(sym['symbol'],sym['name'],sym['pe_ttm'])


#exm = GetStockList(list_host,headers)
#sList = exm.toListByPage()
#print(exm.toNum())
#for i in range(len(sList)):
#    sym = sList[i]
#    print(sym['symbol'],sym['name'],sym['pe_ttm'])
