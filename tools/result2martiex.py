#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import numpy as np
import community
import os
import networkx as nx
data_path= '..'
num_class=37
PROJECT_DIR = "../dataset"
# app name
app = "jpetstore"

method='gdcdvf_output'
method_type='vertical'
with open( os.path.join(PROJECT_DIR, app, "input", "mapping.json")) as f:
    id_mapping = json.load(f)
mapping_id = {v: k for k, v in id_mapping.items()}
from collections import defaultdict

OUTPUT_DIR = os.path.join(PROJECT_DIR, app,"input",method + "_matrix")

if app == "acmeair":
    partition_sizes = [5, 7, 9, 11, 13]  # acmeair
if app == "daytrader":
    partition_sizes = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]  # daytrader #Root
if app == "jpetstore":
    partition_sizes = [3, 5, 7, 9, 11, 13, 15, 17]  # jpetstore #Rootjdiff=3
    # partition_sizes = [3, 5, 7, 9]  # jpetstore #Rootjdiff=3
if app == "plants":
    partition_sizes = [2, 4, 6, 8, 10, 12]  #

for k in partition_sizes:
    parit_ = defaultdict(list)

    with open(os.path.join(PROJECT_DIR, app,method,method_type + "_cluster_assignment__" + str(k) + ".json"),
              'r') as f:
        class_id = json.load(f)


    for i in class_id.keys():
        parit_[str(class_id[i])].append(mapping_id[i])
    sim_martex = np.zeros((num_class, num_class))

    for f in parit_.keys():
        result = parit_[f]
        for i in result:
            for j in result:
                sim_martex[int(i)][int(j)] = 1

    np.savetxt(OUTPUT_DIR + "/results_{0}_{1}.csv".format(method, k), sim_martex, delimiter=',')

