#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Zoey zhu
@file:product_graph.py
@time:2023/04/15
三个图:
1.类与类之间的调用关系：class_class.csv
2.类与类之间的继承关系:class_class_inherit.csv
3.类与业务的关系:class_business.txt
4. 类与数据库的关系，数据库与数据库之间的关系：类-数据库-类关系: class_database_class.txt
"""

import os
import re
import sys
import json
import logging
import subprocess
import pandas as pd
import numpy as np
import networkx as nx
from pathlib import Path
from pdb import set_trace
from collections import defaultdict

# Logging Config



if __name__ == "__main__":

    opt = {
        "use_root": False,
        "keep_return": False,
        "verbose": True,
        "visualize": False,
    }


    print("Run configurations: ")
    # for k, v in opt.items():
    #     print("\t{}: {}".format(k, v), end="\n")
    project_dir = '../'
    bcs_class='bcs_per_class.json'
    maping_path='mapping.json'
    with open(maping_path, 'r') as f:
        id_mapping = json.load(f)
    mapping_id= {v: k for k, v in id_mapping.items()}
    import pathlib
    #第一步：生成 class_class.csv class_class_inherit.csv mapping.json三个文件
    project_dir = pathlib.Path(project_dir)
    opt.update({"datasets_dir": project_dir})
    num_classes=37
    #第二步：生成 class_business_class.txt class_database_class.txt class_file_class.txt
    class_business_class = np.zeros((num_classes, num_classes))  # 调用


    with open(bcs_class, 'r') as f:
        bcs_form = json.load(f)
    bcs=defaultdict(list)
    for i in bcs_form.keys():
        if i == 'Root':
            continue
        class_list=bcs_form[i]
        for j in class_list:
            bcs[j].append(i)

    for i in bcs.keys():
        if i == 'Root':
            continue
        result=bcs[i]
        for j in range(len(result)):
            for k in range(j,len(result)):
                i1=int(mapping_id[result[j]])
                i2=int(mapping_id[result[k]])
                class_business_class[i1][i2] =1
                class_business_class[i2][i1] =1

    np.savetxt('class_business_class.csv', class_business_class, delimiter=',', fmt="%d")

    # class_file_class = np.zeros((num_classes, num_classes))  # 调用

    import re

    # file_name_regex = r"/([^/]+)\.java$"  # 从文件路径中提取文件名的正则表达式
    # with open(file_class, 'r') as f:
    #     file_class = json.load(f)
    # class_file_content=file_class['Files']
    # packge_dict=defaultdict(list)
    # for i in class_file_content.keys():
    #     match = re.search(file_name_regex, i)
    #     con=class_file_content[i][ "package"]
    #
    #     packge_dict[con].append(match.group(1))
    # with open('package_dict.json', 'w') as mapping_file:
    #     json.dump(packge_dict, mapping_file, indent=4)











