#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import os
import re
import csv
from io import StringIO
with open('../dataset/daytrader/daytrader_transaction.json', 'r') as file:
    data = json.load(file)
import re

def extract_tables_from_sql(sql):
    # 匹配INSERT、UPDATE、DELETE和SELECT语句中的表名
    pattern = re.compile(r'(?:INSERT\s+INTO|UPDATE|DELETE\s+FROM|FROM|JOIN)\s+([^\s;]+)', re.IGNORECASE)
    matches = pattern.findall(sql)
    return matches

def extract_content(input_string):
    pattern = re.compile(r'^(.*?)\.java')
    match = pattern.search(input_string)
    if match:
        return match.group(1)
    else:
        return None
from collections import defaultdict
class_table_relation=defaultdict(list)
for j in data:
    if len(j['transactions']) !=0:
        s=j['transactions']
        for f in s:
            trasaction=f['transaction']
            for n in trasaction:
                sql=n['sql']
                stack_trare=n['stacktrace']
                class_list=[]
                for stack in stack_trare:
                    pos_lcaa=stack['position']
                    class_list.append(extract_content(pos_lcaa))
                class_list=list(set(class_list))
                #获取sql语句中涉及的表
                tables = extract_tables_from_sql(sql)
                if len(tables)!=0 and len(class_list)!=0:
                    #建立class和table的关系
                    for class_s in class_list:
                        for table in tables:
                            if table not in class_table_relation[class_s]:
                                class_table_relation[class_s].append(table)
print(class_table_relation)
