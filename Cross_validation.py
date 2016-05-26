#coding: utf-8
import random
import numpy as np

#目的変数１つ用の交差検定関数,引数のfuncにはscikit-learnのモデルクラスを想定
def cross_validation(func, data, times=10):
    random.shuffle(data)
    newx = data[:, :-1]
    newy = data[:, -1:]

    sum=0.0
    for i in range(times):
        accuracy=0.0
        print("%d of %d" % (i+1, times))
        crossnum = np.array([False] * len(data))
        crossnum[i * len(data) / times:(i + 1) * len(data) / times] = True
        func.fit(newx[~crossnum],newy[~crossnum])
        pred=func.predict(newx[crossnum])
        test=newy[crossnum]

        for j in range(len(test)):
            if pred[j]==test[j]:
                accuracy+=1
            #else:
             #   print ("pre:%d test:%d" %(pred[j] , test[j]))
        sum+=accuracy/len(test)
    return sum / times