#!/usr/bin/python
# -*- coding: UTF-8 -*-

from collections import defaultdict
import json

import csv
import os
import  json
from collections import defaultdict
PROJECT_DIR = "../dataset"
import numpy as np
id_class=defaultdict(str)
class_id=defaultdict(int)
# app name
app = "jpetstore"
if __name__ == "__main__":
    PROJECT_DIR_new = "../dataset/"
    # app name
    app_list = ["acmeair", "daytrader", "jpetstore", "plants"]
    app_list = ["jpetstore"]
    for app in app_list:
        method = "fosci_output"

        partition = {}

        print("-------------hierarchical metrics--------------")

        if app == "acmeair":
            partition_sizes = [5, 7, 9, 11, 13]  # acmeair
        if app == "daytrader":
            partition_sizes = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]  # daytrader #Root
        if app == "jpetstore":
            partition_sizes = [3, 5, 7, 9, 11, 13, 15, 17]  # jpetstore #Rootjdiff=3
        if app == "plants":
            partition_sizes = [2, 4, 6, 8, 10, 12]  # plants #Root


        # for k in partition_sizes:
        if 1:
            k=15
            csv_file = os.path.join(PROJECT_DIR_new, app, method,app+"_n_candidate_"+str(k)+"_repeat_1.csv")
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
            with open(os.path.join(PROJECT_DIR_new, app, method+"s","vertical_cluster_assignment__"+str(9)+".json"),'w') as f:
                json.dump(my_dict1,f)# with open('vertical_cluster_assignment_3.json','w') as f:
