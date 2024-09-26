#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zoey zhu
@file:cal_sim_node2.py
@time:2023/04/03
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

import json
data_path= '../dataset/jpetstore'
mapping_path="mapping.json"
with open( mapping_path) as f:
    id_mapping = json.load(f)
mapping_id = {v: k for k, v in id_mapping.items()}
# 获取边的列表

# 将边的节点编号为连续整数

# 生成edge_index

# 1.加载Cora数据集
MAX_VOCAB = 28
# 2.定义模型

# line 模型



# 迭代器
# 优化器

# 3.开始训练


import networkx as nx
import community

# 创建图

from scipy.spatial.distance import cosine
path='class_business_class.csv'
class_class=np.loadtxt(path,dtype=float,delimiter=',')
G = nx.from_numpy_matrix(class_class)

ispartition=False



partition = community.best_partition(G, randomize=False)
from collections import defaultdict
s=defaultdict(int)
# print(partition)
for i in partition.keys():
    s[id_mapping[str(i)]]=partition[i]
#
#
json_data = json.dumps(s)
with open('bsp-jept.json', 'w') as f:
    f.write(json_data)
# with open('Cogcn_op_result/jpetstore/GGRME/result_initwithfile.json', 'w') as f:
#     f.write(json_data)
# with open('Cogcn_op_result/result_embedding_line_1.json', 'w') as f:
#     f.write(json_data)
# 显示图形
# # 可视化节点的embedding
# with torch.no_grad():
#     # 不同类别节点对应的颜色信息
#     colors = [
#         '#ffc0cb', '#bada55', '#008080', '#420420', '#7fe5f0', '#065535',
#         '#ffd700'
#     ]
#
#     model.eval()  # 开启测试模式
#     # 获取节点的embedding向量，形状为[num_nodes, embedding_dim]
#     z = model(torch.arange(data.num_nodes, device=device))
#     # 使用TSNE先进行数据降维，形状为[num_nodes, 2]
#     z = TSNE(n_components=2).fit_transform(z.detach().numpy())
#     y = data.y.detach().numpy()
#
#     plt.figure(figsize=(8, 8))
#
#     # 绘制不同类别的节点
#     for i in range(dataset.num_classes):
#         # z[y==0, 0] 和 z[y==0, 1] 分别代表第一个类的节点的x轴和y轴的坐标
#         plt.scatter(z[y == i, 0], z[y == i, 1], s=20, color=colors[i])
#     plt.axis('off')
#     plt.show()
