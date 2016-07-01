# coding:utf-8

from sklearn import tree
import csv
import numpy as np
import re


#データの読み取り
f=open("adult.data", "r")
data=csv.reader(f)


data=[v for v in data]


for i in range(len(data)):
    for j in range(len(data[0])):
        data[i][j]=data[i][j].replace(" ","")

#adultのデータを生成（String型では決定木を作成できない）
dic_list = [] #辞書のネストを作成
for i in range(len(data[0])):
    dic={}
    dic_list.append(dic)

#ある文字列がfloatに変換可能かどうか調べる正規表現
num_reg = re.compile('^[+-]?(\d*\.\d+|\d+\.?\d*)([eE][+-]?\d+|)\Z')

for i in range(len(data)):
    for j in range(len(data[0])):
        #文字列がfloatに変換不可ならば
        if bool(num_reg.match(data[i][j])) == False:
            if (data[i][j] not in dic_list[j]):
                dic_list[j][data[i][j]]=float(len(dic_list[j])+1)
            data[i][j] = dic_list[j][data[i][j]]
        else:
            data[i][j]=float(data[i][j])

#float型でデータを再生成
cdata=np.array(data, dtype=np.float)
f.close()

#テスト用のデータ読み込み
f=open("adult.test", "r")
test=csv.reader(f)


test=[v for v in test]

for i in range(len(test)):
    for j in range(len(test[0])):
        test[i][j]=test[i][j].replace(" ","")
        test[i][j] = test[i][j].replace(".", "")

for i in range(len(test)):
    for j in range(len(test[0])):
        #文字列がfloatに変換不可ならば
        if bool(num_reg.match(test[i][j])) == False:
            if (test[i][j] not in dic_list[j]):
                dic_list[j][test[i][j]]=float(len(dic_list[j])+1)
            test[i][j] = dic_list[j][test[i][j]]
        else:
            test[i][j]=float(test[i][j])

#float型でデータを再生成
test=np.array(test, dtype=np.float)

np.savetxt("adult_num.data", data,  delimiter=',')
np.savetxt("adult_num.test", test,  delimiter=',')
f.close()
