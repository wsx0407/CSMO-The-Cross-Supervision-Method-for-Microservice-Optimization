#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import  json
from collections import defaultdict
import itertools

PROJECT_DIR = "../dataset"
import numpy as np



id_class=defaultdict(str)
class_id=defaultdict(int)
# app name
app = "jpetstore"
with open(os.path.join(PROJECT_DIR, app, "input", "class_table_rel.json"), 'r') as f:
    class_table_rel_tem = json.load(f)
class_table_rel=defaultdict(list)
for item in class_table_rel_tem.keys():
    class_table_rel[item]=class_table_rel_tem[item]
table_reltion_int = defaultdict(int)
with open(os.path.join(PROJECT_DIR, app, "input", "database_rel.txt"), 'r') as f:
    class_table_relable = f.read()
    class_table_relable = class_table_relable.split("\n")
    for j in class_table_relable:
        if len(j) != 0:
            table = j.split(' ')
            table_reltion_int[(table[0].lower(), table[1].lower())] = 1
            table_reltion_int[(table[1].lower(), table[0].lower())] = 1

class_micro=defaultdict(list)
class_table=defaultdict(list)
for j in class_table_rel.keys():
    class_table[j]=class_table_rel[j]
with open(os.path.join(PROJECT_DIR, app, "input", "mapping.json"), 'r') as f:
    mapping = json.load(f)
for i in mapping.keys():
    id_class[i]=mapping[i]
    class_id[mapping[i]]=int(i)

# 创建一个n*n维度的零矩阵
database_matrix = np.zeros((len(class_id), len(class_id)))
database_matrix_weight = np.zeros((len(class_id), len(class_id)))

for i in range(database_matrix.shape[0]):
    for j in range(database_matrix.shape[1]):
        tablei=class_table_rel[id_class[str(i)]]
        tablej=class_table_rel[id_class[str(j)]]
        #1.求交集
        len_intre=len(list( set(tablei) & set(tablej)))
        #2.组合
        combinations = list(itertools.product(tablei, tablej))
        len_relate=0
        for f in combinations:
            len_relate+=table_reltion_int[f]

        database_matrix_weight[i][j]=len_intre+len_relate
        if len_intre+len_relate!=0:
            database_matrix[i][j]=1
np.savetxt(os.path.join(PROJECT_DIR, app, "input", "database_struct.csv"), database_matrix, delimiter=',')

np.savetxt(os.path.join(PROJECT_DIR, app, "input", "database_struct_weight.csv"), database_matrix_weight, delimiter=',')
