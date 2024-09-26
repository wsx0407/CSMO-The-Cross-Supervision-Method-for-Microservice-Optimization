#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zoey zhu
@file:chance_to_order.py.py
@time:2023/04/29
"""
from collections import defaultdict
import json

import csv

csv_file = 'jpetstore_n_candidate_5_repeat_1.csv'  # 替换为你的 CSV 文件路径
part12 = {}

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        key = row[0]
        value = row[1]
        part12[key] = int(value)





part1 = sorted(part12.keys())
my_dict1={}
for key in part1:
    my_dict1[key]= part12[key]
print(my_dict1)
# with open('vertical_cluster_assignment_3.json','w') as f:
#     json.dump(my_dict1,f)
# with open('vertical_cluster_assignment_5.json','w') as f:
#     json.dump(my_dict2,f)
