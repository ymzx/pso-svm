# -*- coding: utf-8 -*-
# @Time    : 2020/6/2
# @Author  : JWDUAN
# @Email   : 494056012@qq.com
# @File    : xxx.py
# @Software: PyCharm
from sklearn.metrics import confusion_matrix
from config.config import kernel
from sklearn.svm import SVC


def confusionMatrix():
    '''
    理解什么是混淆矩阵
    :return:
    '''
    y_true = [1, 1, 0, 1, 0, 0]
    y_pred = [0, 0, 0, 1, 1, 1]
    C = confusion_matrix(y_true, y_pred)
    print(C)

def predict(data,gamma,c):
    X_train, X_test, y_train, y_test = data
    svclassifier = SVC(kernel=kernel, gamma=gamma, C=c)
    svclassifier.fit(X_train, y_train)
    y_train_pred = svclassifier.predict(X_train)
    y_test_pred = svclassifier.predict(X_test)
    return y_train_pred, y_test_pred

if __name__ == '__main__':
    data = ''
    gamma = ''
    c = ''
    # 补齐上面三个参数内容即可
    predict(data,gamma,c)