#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import os
import networkx as nx

PROJECT_DIR_origin = "../dataset"

def get_stru_metrics(app,target,type):
    with open( os.path.join(PROJECT_DIR_origin, app,'input', "class_table_rel.json"), 'r') as file:
        class_table_rel = json.load(file)

    from collections import defaultdict
    from itertools import product
    import matplotlib.pyplot as plt



    table_reltion=defaultdict(list)
    table_reltion_int=defaultdict(int)
    with open(os.path.join(PROJECT_DIR_origin, app,'input', "database_rel.txt"), 'r') as file:
        class_table_relable = file.read()
        class_table_relable=class_table_relable.split("\n")
        for j in class_table_relable:
            if len(j)!=0:
                table=j.split(' ')
                table_reltion[table[0]].append(table[1])
                table_reltion[table[1]].append(table[0])
                table_reltion_int[(table[0].lower(),table[1].lower())]=1
                table_reltion_int[(table[1].lower(),table[0].lower())]=1
    class_micro=defaultdict(list)
    class_table=defaultdict(list)
    for j in class_table_rel.keys():
        class_table[j]=class_table_rel[j]

    if app == "acmeair":
        partition_sizes = [5, 7, 9, 11, 13]  # acmeair
    if app == "daytrader":
        partition_sizes = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]  # daytrader #Root
    if app == "jpetstore":
        partition_sizes = [3, 5, 7, 9, 11, 13, 15, 17]  # jpetstore #Rootjdiff=3
    if app == "plants":
        partition_sizes = [2, 4, 6, 8, 10, 12]  # plants #Root

    res2=[]
    t_res=[]
    for PA in partition_sizes:
        partition = {}
        try:
            with open(os.path.join(PROJECT_DIR_origin, app,target+ "/"+type+"_cluster_assignment__" + str(PA) + ".json"),
                                  'r') as f:
                partition = json.load(f)
        except:
            continue

        for j in partition.keys():
            class_micro[partition[j]].append(j)
        table_micro=defaultdict(list)
        micro_table=defaultdict(list)
        for j in class_micro.keys():
            for k in class_micro[j]:
                s=class_table[k]
                micro_table[j]+=s
   
        for j in micro_table.keys():
            micro_table[j]=list(set(micro_table[j]))
   
        common_elements = set()
        graph_result=[]
       
        for key, values in micro_table.items():
            for key1, values1 in micro_table.items():
                if key1!=key:
                    common_elements =len(list( set(values) & set(values1)))
                    for f in range(common_elements):
                        graph_result.append((key,key1))
                        # graph_result.append((key1,key))
                    all_combinations = list(product(values, values1))
                    for n in all_combinations:
                        if table_reltion_int[(n[0].lower(),n[1].lower())]==1:
                            graph_result.append((key,key1))
                            # graph_result.append((key1,key))

   
        res2.append(len(graph_result))
        G = nx.Graph()
        G.add_edges_from(graph_result)
       
        communities = list(nx.community.girvan_newman(G))
      
        res=[]
        for i, com in enumerate(communities):
            try:
                modularity = nx.community.modularity(G, com)
                res.append(modularity)
            except:
                res.append(0)
                print('222')
        t_res.append(round(sum(res)/len(res),3)+1)

    return t_res,res2