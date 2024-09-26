#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import  json
from collections import defaultdict
PROJECT_DIR = "../dataset"
import numpy as np



id_class=defaultdict(str)
class_id=defaultdict(int)
# app name
app = "jpetstore"
with open(os.path.join(PROJECT_DIR, app, "input", "bcs_per_class.json"), 'r') as f:
    bcp_data = json.load(f)

with open(os.path.join(PROJECT_DIR, app, "input", "mapping.json"), 'r') as f:
    mapping = json.load(f)
for i in mapping.keys():
    id_class[i]=mapping[i]
    class_id[mapping[i]]=int(i)

class_bussiness=defaultdict(list)
# 创建一个n*n维度的零矩阵
bcp_matrix = np.zeros((len(class_id), len(class_id)))
for cla, bu in bcp_data.items():
    class_bussiness[cla]=bu

for i in range(bcp_matrix.shape[0]):
    for j in range(bcp_matrix.shape[1]):
        bcp_matrix[i][j]=len(list(set(class_bussiness[id_class[str(i)]]) & set(class_bussiness[id_class[str(j)]])))

np.savetxt(os.path.join(PROJECT_DIR, app, "input", "bussiness_struct.csv"), bcp_matrix, delimiter=',')

