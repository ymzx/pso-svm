# pso-svm
粒子群算法优化支持向量机


## 1 使用方法
```
python  pso_svm.py
```

## 2 目录结构
```
|-- .idea  
|   |-- encodings.xml  
|   |-- misc.xml  
|   |-- modules.xml  
|   |-- pso-svm-master.iml  
|   `-- workspace.xml  
|-- LICENSE  
|-- README.md   # 说明文档
|-- config      # 数据、SVM及PSO算法参数配置 
|   |-- __pycache__  
|   |   `-- config.cpython-36.pyc  
|   `-- config.py    
|-- data        # 数据存放  
|   |-- Statlog_heart_Data.csv  
|   `-- heart.dat  
|-- pso_svm.py  # pso_svm算法实现
|-- test.py     # svm功能测试
`-- utils.py    # 读取数据 画图可视化
```

## 3 算法介绍

```
粒子群优化算法（Particle Swarm Optimization，PSO）属于进化算法的一种，是通过模拟鸟群捕食行为设计的。  
从随机解出发，通过迭代寻找最优解，通过适应度来评价解的质量。PSO初始化为一群随机粒子(随机解)，然后通过迭代找到最优解。
所有的粒子具有位置(particle_position_vector)和速度(velocity_vector)两个属性。 
在每一次迭代中，粒子通过粒子本身所找到的最优解pbest和整个种群目前找到的最优解全局极值gbest来更新。

PSO算法用于寻找适用于SVM模型的核函数类型步骤如下：（pso_svm.py）
Step 1：从config读取粒子群参数配置，进行初始化
Step 2：将每个粒子的个体极值设置为当前位置，利用适应度函数(fitness_function)计算每个粒子的适应度值，
        取适应度好对应的个体极值作为最初的全局极值
Step 3：按照粒子的位置和速度更新公式进行迭代计算，更新粒子的位置和速度；
Step 4：按照粒子的适应度函数(fitness_function)计算每次迭代后每个粒子的适应度值，
        将每个粒子的适应度值与其个体极值的适应度值(pbest_fitness_value)作比较，如果更优的话，则更新个体极值，否则保留原值；
        将更新后的每个粒子的个体极值与全局极值(gbest_fitness_value)比较，如果更优的话，则更新全局极值，否则保留原值；
Step 5：迭代至满足终止条件，达到最大迭代次数，得到使得模型最佳的参数组合

```



