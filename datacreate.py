#coding: utf-8
__author__ = 'umeco'

import seaborn as sns
import pandas as pd
import csv
import re
import random


#データの読み取り
f=open("adult.data", "r")
data=csv.reader(f)

data=[v for v in data]


for i in range(len(data)):
    for j in range(len(data[0])):
        data[i][j]=data[i][j].replace(" ","")


#ある文字列がfloatに変換可能かどうか調べる正規表現
num_reg = re.compile('^[+-]?(\d*\.\d+|\d+\.?\d*)([eE][+-]?\d+|)\Z')

for i in range(len(data)):
    for j in range(len(data[0])):
        #文字列がfloatに変換不可ならば
        if bool(num_reg.match(data[i][j])) == True:
            data[i][j]=float(data[i][j])

#データフレーム作成
data=pd.DataFrame(data)
data.columns = ['age',"workclass","fnlwgt","education","education-num","marital-status","occupation","relationship","race","sex","capital-gein","capital-loss","hours-per-week","native-country","money"]

#数値型を先頭に、文字列型を後方に入れ替える
data=data.ix[:,[0,2,4,10,11,12,1,3,5,6,7,8,9,13,14]]
