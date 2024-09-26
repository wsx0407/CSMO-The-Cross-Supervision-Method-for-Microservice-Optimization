#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import numpy as np
import community
import os
from tools.Laplace import normalize_adj
import matplotlib.pyplot as plt

import networkx as nx
import torch
data_path= '..'
epoch=500
weight_decay=0.0
learning_rate=0.0001
adam_epsilon=1e-8
max_steps=-1
PROJECT_DIR = "../dataset"
# app name
app = "jpetstore"
method='gdcdvf_output'
with open( os.path.join(PROJECT_DIR, app, "input", "mapping.json")) as f:
    id_mapping = json.load(f)
mapping_id = {v: k for k, v in id_mapping.items()}
from collections import defaultdict
from mlp import NeuralNetwork
origin_DIR = os.path.join(PROJECT_DIR, app,"input",method + "_matrix")
SUPERVISE_DIR = os.path.join(PROJECT_DIR, app,"input",'supervise')
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if app == "acmeair":
    partition_sizes = [5, 7, 9, 11, 13]  # acmeair
if app == "daytrader":
    partition_sizes = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]  # daytrader #Root
if app == "jpetstore":
    partition_sizes = [3, 5, 7, 9, 11, 13, 15, 17]  # jpetstore #Rootjdiff=3
if app == "plants":
    partition_sizes = [2, 4, 6, 8, 10, 12]  #

call_relation = np.loadtxt(os.path.join(PROJECT_DIR,  app,"input","supervise","call_relation.csv"), dtype=float, delimiter=',')#其他方法的结果
call_relation=normalize_adj(call_relation)#拉普拉斯标准化
call_relation = torch.from_numpy(call_relation).float()
call_relation = torch.unsqueeze(call_relation, 0)

business_relation = np.loadtxt(os.path.join(PROJECT_DIR,  app,"input","supervise","bussiness_struct.csv"), dtype=float, delimiter=',')#其他方法的结果
business_relation=normalize_adj(business_relation)#拉普拉斯标准化
business_relation = torch.from_numpy(business_relation).float()
business_relation = torch.unsqueeze(business_relation, 0)
print(business_relation.shape[0])

table_relation = np.loadtxt(os.path.join(PROJECT_DIR,  app,"input","supervise","database_struct_weight.csv"), dtype=float, delimiter=',')#其他方法的结果
table_relation=normalize_adj(table_relation)#拉普拉斯标准化
table_relation = torch.from_numpy(table_relation).float()
table_relation = torch.unsqueeze(table_relation, 0)

for k in partition_sizes:
    
    origin_result = np.loadtxt(os.path.join(origin_DIR,   "results_"+method+"_"+str(k) + ".csv"), dtype=float, delimiter=',')#其他方法的结果
    dim_=origin_result.shape[0]
    origin_result=normalize_adj(origin_result)#拉普拉斯标准化
    origin_result = torch.from_numpy(origin_result).float()
    origin_result = torch.unsqueeze(origin_result, 0)
    
    model = NeuralNetwork(dim_)
    model.zero_grad()
    no_decay = ['bias', 'LayerNorm.weight']

    optimizer_grouped_parameters = [
        {'params': [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)],
         'weight_decay': weight_decay},
        {'params': [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
    ]
    optimizer = torch.optim.AdamW(optimizer_grouped_parameters, lr=learning_rate, eps=adam_epsilon)

    loss_list=[]
    
    for j in range(epoch):
        output = model(origin_result)

        # 打印输出矩阵的形状
        loss = torch.nn.functional.mse_loss(output, call_relation) + torch.nn.functional.mse_loss(output,
                                                                                    business_relation) + torch.nn.functional.mse_loss(
        output, table_relation)
        loss.backward()

        optimizer.step()
        optimizer.zero_grad()

        # scheduler.step()
        loss_data = loss.detach().cpu().numpy()
        loss_list.append(loss_data)
    iterations = range(1, len(loss_list) + 1)
    plt.plot(iterations, loss_list, '-o')
    plt.title('Loss Change During Training')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.grid(True)
    plt.show()
    output = model(origin_result)
    output = output.squeeze()
    output=output.detach().numpy()
    print(output.shape)
    np.savetxt(os.path.join(PROJECT_DIR, app, "output", method,method+"_"+str(k) + "_.csv"), output, delimiter=',')

 