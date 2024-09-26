#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zoey zhu
@file:get_buss.py
@time:2023/05/05
"""

import json
with open('bcs_per_class.json','r') as f:
    bcs_per_class = json.load(f)
bs_list=[]
for j in bcs_per_class.keys():
    bs_list+=(bcs_per_class[j])
print(len(list(set(bs_list))))
