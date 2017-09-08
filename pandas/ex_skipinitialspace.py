#!/usr/bin/env python

import csv
import sys
import scipy
import logging
import numpy as np
import matplotlib
import sklearn
import datetime
import pandas as pd
import tensorflow as tf
import sc_util

sc_util.initialize(logging.INFO)

lines = '''222, 333'''.splitlines()

#list
print (lines)
for i in lines:
    print (i)

print ("="*10 + " skipinitiallspaces=True")
for l in  csv.reader(lines, delimiter=',', quoting=csv.QUOTE_NONE, skipinitialspace=True):
    print (l)
    for i in l:
        print (i)

print ("="*10 + " skipinitiallspaces=False(default)")
for l in  csv.reader(lines, delimiter=',', quoting=csv.QUOTE_NONE, skipinitialspace=False):
    print (l)
    for i in l:
        print (i)

'''
# ./ex_skipinitialspace.py 
['222, 333']
222, 333
========== skipinitiallspaces=True
['222', '333']
222
333
========== skipinitiallspaces=False(default)
['222', ' 333']
222
 333
'''
