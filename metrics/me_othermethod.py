#!/usr/bin/python
# -*- coding: UTF-8 -*-


import metrics_util
import json
import os
import csv


def gen_partitons(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    count = len(lines)
    partitions = {}

    index = 0
    for line in lines:
        class_str = line.split("=")[1]
        classes = class_str.split(",")
        for cls in classes:
            if cls not in partitions:
                partitions[cls.strip()] = index

        index += 1

    return partitions, count


def gen_mono2micro_format(datasets_runtime, application, count, partitions):
    #     partition = {}
    #     for key in partitions:
    #         partition[key] = str(partitions[key])

    with open(datasets_runtime + application + "/bunch_output/" + application + "_" + str(count) + ".json", "w") as f:
        json.dump(partitions, f, indent=4)


if __name__ == "__main__":

    PROJECT_DIR_origin = "../dataset"
    PROJECT_DIR_new = "../dataset/"

    # app name

    app_list = ["acmeair", "daytrader", "jpetstore", "plants"]
    app_list = ["jpetstore"]

    for app in app_list:
        # app = "acmeair"
        # app = "daytrader"
        # app = "jpetstore"
        # app = "plants"

        benchmark_type = "best_coupling_cluster"
        method = "spectral"

        ROOT = 'Root'  # $Root$

        # from mono2micro output dir get partition file, bcs_per_class, runtime_call_volume
        OUTPUT_DIR = os.path.join(PROJECT_DIR_new, app, benchmark_type + "_output")

        bcs_per_class = {}
        with open(os.path.join(PROJECT_DIR_origin, app, "mono2micro_output", "bcs_per_class.json"), 'r') as f:
            bcs_per_class = json.load(f)

        runtime_call_volume = {}
        with open(os.path.join(PROJECT_DIR_origin, app, "mono2micro_output", "runtime_call_volume.json"), 'r') as f:
            runtime_call_volume = json.load(f)

        partition = {}

        OUTPUT_DIR = os.path.join(PROJECT_DIR_new, app,benchmark_type)
        print("-------------hierarchical metrics--------------")

        if app == "acmeair":
            partition_sizes = [5, 7, 9, 11, 13]  # acmeair
        if app == "daytrader":
            partition_sizes = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]  # daytrader #Root
        if app == "jpetstore":
            partition_sizes = [3, 5, 7, 9, 11, 13, 15, 17]  # jpetstore #Rootjdiff=3
        if app == "plants":
            partition_sizes = [2, 4, 6, 8, 10, 12]  # plants #Root


        res=[]
        for k in partition_sizes:
                partition = {}
                with open(os.path.join(OUTPUT_DIR,method + "_cluster_assignment__" + str(k) + ".json"),
                          'r') as f:
                    partition = json.load(f)

                class_bcs_partition_assignment, partition_class_bcs_assignment = metrics_util.gen_class_assignment(
                    partition, bcs_per_class)
                bcs = metrics_util.business_context_purity(partition_class_bcs_assignment)
                icp = metrics_util.inter_call_percentage(ROOT, class_bcs_partition_assignment, runtime_call_volume)
                sm = metrics_util.structural_modularity(partition_class_bcs_assignment, runtime_call_volume)
            
                cohesion,coupling = metrics_util.co_cp(partition_class_bcs_assignment, runtime_call_volume)

                mq = metrics_util.modular_quality(ROOT, partition_class_bcs_assignment, runtime_call_volume)
                ifn = metrics_util.interface_number(ROOT, partition_class_bcs_assignment, runtime_call_volume)
                ned = metrics_util.non_extreme_distribution(partition_class_bcs_assignment)

                print("# partition size:", k)
                print(str(k) + "," + str(bcs) + "," + str(icp) + "," + str(sm) + "," + str(mq) + "," + str(
                    ifn) + "," + str(ned))
                res.append([k,bcs,icp,sm,cohesion,coupling*ned,mq,ifn,ned])

        with open(OUTPUT_DIR + "/results_{0}_{1}.csv".format(benchmark_type, app), "a") as csvfile:

            writer = csv.writer(csvfile)
            writer.writerow([
                    "partition_size",
                    "↓ business_context_purity",
                    "↓inter_call_percentage",
                    "↑structural_modularity",
                    "↑cohesion",
                    "↓coupling",
                    "↑modular_quality",
                    "↓interface_number",
                    "↓non_extreme_distribution",
                ])
            for i in res:
                writer.writerow(i)
