#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zoey zhu
@file:chance_to_order.py.py
@time:2023/04/29
"""
from collections import defaultdict
import json

with open('jpetstore_4.json','r') as f:
    part12=json.load(f)

with open('jpetstore_11.json','r') as f:
    part22=json.load(f)

part1 = sorted(part12.keys())
part2 = sorted(part22.keys())
my_dict1={}
for key in part1:
    my_dict1[key]= part12[key]
my_dict2={}
for key in part2:
    my_dict2[key]= part22[key]
# with open('vertical_cluster_assignment_3.json','w') as f:
#     json.dump(my_dict1,f)
# with open('vertical_cluster_assignment_5.json','w') as f:
#     json.dump(my_dict2,f)
id_class=defaultdict(list)
id_class2=defaultdict(list)
for key in part1:
    id_class[part12[key]].append(key)
for key in part2:
    id_class2[part22[key]].append(key)
for j in id_class:
    print(id_class[j])
print('--------')
for f in id_class2:
    print(id_class2[f])