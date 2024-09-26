#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import numpy as np

PROJECT_DIR = "../dataset"
# app name
app = "jpetstore"

type='sim_bcp'


if type=='sim_bcp':
    C=np.loadtxt(os.path.join(PROJECT_DIR, app, "input", "bussiness_struct.csv"), dtype=float, delimiter=',')
elif type=='sim_cop' or type=='sim_cop':
    A = np.loadtxt(os.path.join(PROJECT_DIR, app, "input", "struct.csv"), dtype=float, delimiter=',')
    B = np.loadtxt(os.path.join(PROJECT_DIR, app, "input", "dy_struct.csv"), dtype=float, delimiter=',')
    C = A + B
sim_matrix = np.zeros((C.shape[0], C.shape[0]))

for i in range(sim_matrix.shape[0]):  # 遍历行
    for j in range(sim_matrix.shape[1]):  # 遍历列
        element = C[i, j]  # 获取当前位置的元素值
        if type=='sim_coh' or type=='sim_bcp':
            cla_sum=np.sum(C[i])+np.sum(C[:, j])
            if cla_sum!=0:
                sim=element/cla_sum
            else:
                sim=0
            sim_matrix[i][j]=sim
        elif type=='sim_cop':
            sim_matrix[i][j]=element


np.savetxt(os.path.join(PROJECT_DIR, app, "input", type+".csv"), sim_matrix, delimiter=',')
