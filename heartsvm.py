import csv
import random
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from time import time
import datetime

def change_float(row):
    out = [float(i) for i in row]
    return out

 #读取并分组
with open("Statlog_heart_Data.csv",'r')as file:
    reader = csv.reader(file)
    datas = [row for row in reader]

datas = datas[1:]
datas = [change_float(row) for row in datas]

data= [ row[0:-2] for row in datas]
lables=[row[-2] for row in datas]

x = np.array(data)
y = np.array(lables)

train_data, test_data, train_target, test_target = train_test_split(x,y,test_size=0.3,random_state=420)

#数据标准化
stdScaler = StandardScaler().fit(train_data)
train_dataStd = stdScaler.transform(train_data)
test_dataStd = stdScaler.transform(test_data)

#分别建立四种类型的核函数的SVM模型，并比较准确率
Kernel = ["linear","poly","rbf","sigmoid"]
for kernel in Kernel:
    time0 = time()
    clf=SVC(kernel=kernel,gamma="auto",degree=3,cache_size=1000).fit(train_dataStd,train_target)
    test_target_pred = clf.predict(test_dataStd)
    correct = np.sum(test_target_pred == test_target)
    print('预测对的结果数目为：', correct)
    print('预测错的的结果数目为：', test_target.shape[0] - correct)
    print('预测结果准确率为：', correct / test_target.shape[0])
    print(datetime.datetime.fromtimestamp(time()-time0).strftime("%M:%S:%f"))
    print('\n')
         
# 建立准确率较高的SVM模型
svm = SVC(kernel="poly").fit(train_dataStd,train_target)
print('建立的SVM模型为：\n',svm)

## 预测训练集结果
test_target_pred = svm.predict(test_dataStd)

# 求出预测和真实一样的数目
correct = np.sum(test_target_pred == test_target )
print('预测对的结果数目为：', correct)
print('预测错的的结果数目为：', test_target.shape[0]-correct)
print('预测结果准确率为：', correct/test_target.shape[0])

#画图
list1=[]
list2=[]
list3=[]
for i in range(len(test_data)):
    xx=int((test_data[i])[0])
    list1.append(xx)
    x=list1
    yy=int((test_target[i]))
    list2.append(yy)
    y=list2

x1=list1
for i in range(len(test_target_pred)):   
    yy1=int(test_target_pred[i])
    list3.append(yy1)
    y1=list3

#加上横轴和纵轴标签
plt.xlabel("testsample")
plt.ylabel("category_label")
#绘制散点图，并加上标签
plt.scatter(x,y,label="really",marker="+")
plt.scatter(x1,y1,label="predicted",marker="x")
plt.legend()
plt.show()