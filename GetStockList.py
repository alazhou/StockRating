#!/home/shijiezhou/anaconda3/bin/python

import urllib.request,urllib.error
import urllib.parse
import requests
import sys
from urllib import request
import json
import time

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
    def toListByPage(self,list_host,page):
        self.list_host =list_host[0]+page+list_host[2]
#        print(self.list_host)
        req = request.Request(self.list_host,headers = self.headers)
        res_data = request.urlopen(req)
        jRes = res_data.read().decode('utf-8')
        sData = json.loads(jRes)
        quota = sData.pop('data')
        self.count = quota.pop('count')
        stock_list = quota.pop('list')
#        print(stock_list)
        return stock_list
    def toNum(self):
        print("stock list have %5d stocks"%self.count)
        return self.count;
    def toPrint(self,sList):
        for i in range(len(sList)):
            sym = sList[i]
            print(sym['symbol'],sym['name'],sym['pe_ttm'])

class StockDetials(QuoteData):
    def __init__(self,host_lst,req_headers):
        QuoteData.__init__(self)
        self.host = host_lst[0]+self.stockid+host_lst[2]
        self.headers = req_headers
    def GetStock(self,host_lst,stockid):
        self.host = host_lst[0]+stockid+host_lst[2]
        time.sleep(1)
        req = request.Request(self.host,headers = self.headers)
#        print(self.host)
        res_data = request.urlopen(req)
        jRes = res_data.read().decode('utf-8')
        sData = json.loads(jRes)
        quota = sData.pop('data')
        quota = quota.pop('quote')
        return quota
    def PrintStock(self,quota):
        print("<{:^8}>".format(quota['name']))
        for (k,v) in quota.items():
            if k == 'symbol' or k == 'pb' or k == 'pe_ttm' or k == 'pe_forecast' or k == 'pe_lyr':
                print("[{: ^12}]:".format(k),v)
            if k == 'current' or k == 'low52w' or k == 'high52w':
                print("[{: ^12}]:".format(k),v)

class PutAvaiStock:
    def __init__(self,dtls):
        self.__dict__['sym']     = dtls['symbol']
        self.__dict__['name']    = dtls['name']
        self.__dict__['current'] = dtls['current']
        self.__dict__['high52w'] = dtls['high52w']
        self.__dict__['low52w']  = dtls['low52w']
        self.__dict__['pb']      = dtls['pb']
        self.__dict__['pe_lyr']  = dtls['pe_lyr']
        self.__dict__['pe_ttm']  = dtls['pe_ttm']
        self.__dict__['pe_forecast']  = dtls['pe_forecast']
        pass
    def __peok(self,peH):
        if self.__dict__['pe_ttm'] > 0 and self.__dict__['pe_ttm'] < peH:
            if self.__dict__['pe_forecast'] > 0 and self.__dict__['pe_forecast'] < peH:
                if self.__dict__['pe_lyr'] > 0 and self.__dict__['pe_lyr'] < peH:
                    return True
        return False        
    def __pbok(self,pbH):
        if self.__dict__['pb'] > 0 and self.__dict__['pb'] < pbH:
            return True
        else:
            return False
            
    def toFilter(self,pbH,peH):
        #print(self.__dict__['sym'])
        #print(self.__dict__['name'])
        #print(self.__dict__['pe_ttm'])
        #print("%f"%pbH)
        if self.__pbok(pbH) and self.__peok(peH):
            print("hit!! %s"%self.__dict__['name'])
            #final_list.append(self.__dict__)
            return True #self.__dict__.clear()
    def ScoreRate(self):
        base      = self.__dict__['low52w']
        riseRatio = self.__dict__['current']/self.__dict__['low52w']-1
        pb = self.__dict__['pb']
        pe = self.__dict__['pe_ttm']
        P1 = (0.5-riseRatio)*2*33
        if pb < 1:
            P2 = 33
        else:
            P2 = (pb - 1)*33
        if pe < 10:
            P3 = 33
        else:
            P3 = (pe -10)/10*33
        return P1+P2+P3

    def PrintFinalList(self):
        print(final_list)

