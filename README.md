# ruomu-part  方法介绍


## 文件目录
```
- dataset 数据集
  - jpetstore  目前只针对jpetstore 进行了实验
    - class_table_rel.json  类与数据库表的关系
    - database.txt  数据表
     - database_rel.txt 数据表之间相互关系
 - jpetstore input
    - struct.csv  静态调用
    - bussiness_struct.csv  基于功能业务关联关系
     - database_struct.csv  基于数据表关联关系的对应关系
     - database_struct_weight.csv 基于数据表关联关系的对应关系（权重）
     - dy_struct.csv  动态调用

- model 方法
  - mlp  简单的神经网络模型
  - op_model  优化模型
  
- metrics 评估指标
  - me.py  主要计算各个指标的文件
  -  structural_metrics.py  表关联关系次数（新增指标）
  
- cluster 聚类算法（对矩阵后聚类）
  - Spect.py  谱聚类
  -  louvain.py  louvain算法（不定义分区数量）
- tools 工具包
   -result2martiex.py 将现有结果转换为邻接矩阵
```

## 输入矩阵

- 类与类之间调用关系：静态调用和动态调用，相加
- 类与类之间基于功能业务的对应关系：关系=1
- 类与类之间基于数据表的关系：两个类，要么存在相同的表，要么表间存在外键关系，相同

- 其他拆分结果转换为矩阵，划分为同一个微服务，彼此互相连接，0，1
## 评价指标：微服务间数据库事务`
- 根据微服务包含的类获取对应的数据表分区结果
- 计算微服务之间基于数据表的关联关系数量（相同数据表、外键关联）
## 使用方法
- 处理好数据集
- 在toos/result2martiex中将其他结果转换为矩阵
- 运行model/op_model，训练模型
- 运行cluster/spect,进行分区
- 运行metrics/me，统计结果
# CSMO-The-Cross-Supervision-Method-for-Microservice-Optimization
# CSMO-The-Cross-Supervision-Method-for-Microservice-Optimization
