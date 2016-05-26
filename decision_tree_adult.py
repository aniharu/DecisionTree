# coding:utf-8

from sklearn import tree
import csv
import numpy as np
import Cross_validation
import re


#データの読み取り
f=open("adult.data", "r")
data=csv.reader(f)

data=[v for v in data]
data.pop()

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

#整数型でデータを再生成
cdata=np.array(data, dtype=np.float)

clf = tree.DecisionTreeClassifier()
print("Cross validation: "+str(Cross_validation.cross_validation(clf,cdata) * 100.0))



#テスト用のデータ読み込み
f=open("adult.test", "r")
test=csv.reader(f)

test=[v for v in test]
test.pop()

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

#整数型でデータを再生成
test=np.array(test, dtype=np.float)
clf = tree.DecisionTreeClassifier()
clf.fit(cdata[:,:-1],cdata[:,-1:])
pre=clf.predict(test[:,:-1])
accuracy=0.0
for j in range(len(pre)):
    if int(pre[j]) == int(test[j][14]):
        accuracy += 1
print "test acculacy: "+ str(accuracy / len(pre)*100)