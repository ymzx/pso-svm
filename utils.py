# -*- coding: utf-8 -*-
# @Time    : 2020/6/2
# @Author  : JWDUAN
# @Email   : 494056012@qq.com
# @File    : utils.py
# @Software: PyCharm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np


def plot(position):
    x = []
    y = []
    for i in range(0,len(position)):
        x.append(position[i][0])
        y.append(position[i][1])
    colors = (0,0,0)
    plt.scatter(x, y, c = colors, alpha = 0.1)
    plt.xlabel('C')
    plt.ylabel('gamma')
    plt.axis([0,10,0,10])
    plt.gca().set_aspect('equal', adjustable='box')
    return plt.show()

def data_handle_v2(data_path):
    colnames = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'y']
    data = pd.read_csv(data_path, sep=' ', header=None, names=colnames)
    X = data.drop('y', axis=1)
    X = (X - X.mean()) / X.std()
    y = data['y']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    return X_train, X_test, y_train, y_test

def data_handle_v1(csv_data_path):
    def change_float(row):
        out = [float(i) for i in row]
        return out
    # 读取并分组
    with open(csv_data_path, 'r')as file:
        reader = csv.reader(file)
        datas = [row for row in reader]
    datas = datas[1:]
    datas = [change_float(row) for row in datas]
    data = [row[0:-2] for row in datas]
    lables = [row[-2] for row in datas]
    x = np.array(data)
    y = np.array(lables)
    ###数据先归一化,待做。。。###
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=420)
    return X_train, X_test, y_train, y_test