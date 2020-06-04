# -*- coding: utf-8 -*-
# @Time    : 2020/6/2
# @Author  : JWDUAN
# @Email   : 494056012@qq.com
# @File    : config.py
# @Software: PyCharm

# 数据源
data_src = '1'
if data_src == '1':
    data_path = 'data/heart.dat'
elif data_src == '2':
    data_path = 'data/Statlog_heart_Data.csv'

# 粒子群算法参数配置
class args:
    W = 0.5 # 惯性权重
    c1 = 0.2 # 局部学习因子
    c2 = 0.5 # 全局学习因子
    n_iterations = 10 # 迭代步数
    n_particles = 100 # 粒子数

# SVM配置
kernel = 'rbf' # ["linear","poly","rbf","sigmoid"]