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

csv_file = 'daytrader_n_candidate_13_repeat_0.csv'  # 替换为你的 CSV 文件路径
part12 = {}

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        key = row[0]
        value = row[1]
        part12[key] = int(value)




print(part12)
# part1 = sorted(part12.keys())
# part2 = sorted(part22.keys())
# my_dict1={}
# for key in part1:
#     my_dict1[key]= part12[key]
# my_dict2={}
# for key in part2:
#     my_dict2[key]= part22[key]
# # with open('vertical_cluster_assignment_3.json','w') as f:
# #     json.dump(my_dict1,f)
# # with open('vertical_cluster_assignment_5.json','w') as f:
# #     json.dump(my_dict2,f)
# id_class=defaultdict(list)
# id_class2=defaultdict(list)
# for key in part1:
#     id_class[part12[key]].append(key)
# for key in part2:
#     id_class2[part22[key]].append(key)
# print('0',id_class[0],id_class2[0])
# print('--------')
# print(id_class[1],id_class2[1])
# print('1','--------')
# print('2',id_class[2],id_class2[2])
# print('--------')
# print(id_class2[3],id_class2[4])