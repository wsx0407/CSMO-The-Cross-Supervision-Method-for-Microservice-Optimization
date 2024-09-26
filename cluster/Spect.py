from sklearn.cluster import SpectralClustering
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler

from sklearn.impute import SimpleImputer
from sklearn.metrics.pairwise import cosine_similarity

import sys
sys.path.append('../')

from tools.Laplace import normalize_adj
from numpy.core.numeric import asarray

PROJECT_DIR = "../dataset"
app = "daytrader"
cluster_data='cargo_output'
import json
if app == "acmeair":
    n_clusters_list = [5, 7, 9, 11, 13]  # acmeair
if app == "daytrader":
    n_clusters_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]  # daytrader #Root
    # n_clusters_list =  [3, 5, 7, 9, 10, 13, 15, 17, 19, 21, 23] # daytrader #Root
    # n_clusters_list = [3, 5, 7, 9, 10, 13, 15, 17, 19, 21, 23]
    n_clusters_list = [3, 4, 5, 6, 7, 8] # cargo


if app == "jpetstore":
    n_clusters_list = [3, 5, 7, 9, 11, 13, 15, 17]  # jpetstore #Rootjdiff=3
    n_clusters_list = [2, 3, 4, 5]
if app == "plants":
    n_clusters_list = [2, 4, 6, 8, 10, 12]  # plants #Root

for n_clusters in n_clusters_list:
    similarity_matrix = np.loadtxt(os.path.join(PROJECT_DIR, app, "output", cluster_data,cluster_data+"_"+str(n_clusters)+".csv"), dtype=float, delimiter=',')
    sc = SpectralClustering(n_clusters=n_clusters, affinity='precomputed')
    try:
        similarity_matrix=np.round(similarity_matrix,2)
        labels = sc.fit_predict(similarity_matrix)
    except:
        similarity_matrix = np.round(similarity_matrix, 1)
        labels = sc.fit_predict(similarity_matrix)

    print("# n_clusters = {0}, Cluster labels for each sample: {1}\n".format(n_clusters, labels))

    file_index = open('../dataset/' + app + '/input/mapping.json',
                      'r')
    map_index = json.loads(file_index.read())
    file_index.close()

    cluster_result = {}

    for i in range(labels.shape[0]):
        cluster_result[map_index[str(i)]] = int(labels[i])


    print('File store path:', "../dataset/{0}/output/{1}/{3}_cluster_assignment_{2}.json".format(
                 app, cluster_data, str(n_clusters), cluster_data))

    with open("../dataset/{0}/output/{1}/{3}_cluster_assignment_{2}.json".format(
                 app, cluster_data, str(n_clusters), cluster_data), 'a') as tf:
        json.dump(cluster_result, tf, indent=1)
