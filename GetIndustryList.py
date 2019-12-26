#!/home/shijiezhou/anaconda3/bin/python
import xmltodict
import json
import sys
import os


class GetIndustryList:
    def __init__(self,filename):
        self.fp       = filename
        self.namelist = []
        self.codelist = []
        self.indlist  = dict(zip(self.namelist,self.codelist))
#        print(self.indlist)
    def __formatdata(self):
        fp = open(self.fp,"r")
        convertDict = xmltodict.parse(fp.read())
        fp.close()
        jsonData = json.dumps(convertDict)
        jsonData = json.loads(jsonData)
        jsonData = jsonData.pop('ul')
        listData = jsonData.pop('li')
        return listData
    def toDict(self):
        listData = self.__formatdata()
        self.namelist = []
        self.codelist = []
        for i in range(len(listData)):
#            print(listData[i]['a']['@title'],listData[i]['a']['@data-level2code'])
            self.namelist.append(listData[i]['a']['@title'])
            self.codelist.append(listData[i]['a']['@data-level2code'])
        return (dict(zip(self.namelist,self.codelist)))
    def toList(self):
        listData = self.__formatdata()
        self.namelist = []
        self.codelist = []
        for i in range(len(listData)):
#            print(listData[i]['a']['@title'],listData[i]['a']['@data-level2code'])
            self.namelist.append(listData[i]['a']['@title'])
            self.codelist.append(listData[i]['a']['@data-level2code'])
        return (self.codelist)



#name = sys.argv[1]

#gil = GetIndustryList(name)
#IndList = gil.toDict()
#print(IndList)
#code = gil.toList()
#print(code)

#with open("ind3.xml","r") as fd:



#for i in range(len(listData)):
#	print(listData[i]['a']['@title'],listData[i]['a']['@data-level2code'])
#	list1.append(listData[i]['a']['@title'])
#	list2.append(listData[i]['a']['@data-level2code'])
#	fpw.write(listData[i]['a']['@title'])
#	fpw.write('   ')
#	fpw.write(listData[i]['a']['@data-level2code'])
#	fpw.write('\n')


#industryDict = dict(zip(list1,list2))
#print(industryDict)
