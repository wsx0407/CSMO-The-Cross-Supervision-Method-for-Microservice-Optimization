#!/usr/bin/python
# -*- coding: UTF-8 -*-


from collections import defaultdict

# 给定的字典
data_dict = defaultdict(list, {1: ['accountejb', 'keygenejb', 'orderejb', 'accountprofileejb', 'holdingejb', 'quoteejb'], 4: ['quoteejb', 'keygenejb'], 2: [], 3: [], 0: []})

common_elements = set()
graph_result=[]
for key, values in data_dict.items():

    for key1, values1 in data_dict.items():
        if key1!=key:
            common_elements = set(values) & set(values1)
            for f in range(len(common_elements)):
                graph_result.append((key,key1))
                graph_result.append((key1,key))

print(graph_result)

import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6), (7, 8), (8, 9)])

communities = list(nx.community.girvan_newman(G))

for i, com in enumerate(communities):
    modularity = nx.community.modularity(G, com)
    print(f"Community {i+1}: Modularity = {modularity}")