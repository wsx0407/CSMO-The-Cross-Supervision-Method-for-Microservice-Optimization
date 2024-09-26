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
with open(os.path.join(PROJECT_DIR, app, "input", "runtime_call_volume.json"), 'r') as f:
    runtime_call_volume = json.load(f)

with open(os.path.join(PROJECT_DIR, app, "input", "mapping.json"), 'r') as f:
    mapping = json.load(f)
for i in mapping.keys():
    id_class[i]=mapping[i]
    class_id[mapping[i]]=int(i)

# 创建一个n*n维度的零矩阵
dy_matrix = np.zeros((len(class_id), len(class_id)))
for call, volume in runtime_call_volume.items():
    src, target = call.split("--")
    c1=class_id[src]
    c2=class_id[target]
    dy_matrix[c1][c2]+=volume
np.savetxt(os.path.join(PROJECT_DIR, app, "input", "dy_struct.csv"), dy_matrix, delimiter=',')

