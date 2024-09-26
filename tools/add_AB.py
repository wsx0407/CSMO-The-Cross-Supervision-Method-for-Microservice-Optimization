#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import numpy as np

PROJECT_DIR = "../dataset"
# app name
app = "jpetstore"
type='call_relation'

A = np.loadtxt(os.path.join(PROJECT_DIR, app, "input", "struct.csv"), dtype=float, delimiter=',')
B = np.loadtxt(os.path.join(PROJECT_DIR, app, "input", "dy_struct.csv"), dtype=float, delimiter=',')
C = A + B



np.savetxt(os.path.join(PROJECT_DIR, app, "input", type+".csv"), C, delimiter=',')
