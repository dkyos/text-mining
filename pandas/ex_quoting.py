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


#lines = '''"AAA", "BBB", "Test, Test", "CCC" "111", "222, 333", "XXX", "YYY, ZZZ"'''.splitlines()
lines = '''"222, 333"'''.splitlines()

#list
print (lines)
for i in lines:
    print (i)

#for l in  csv.reader(lines, quotechar='"', delimiter='|', quoting=csv.QUOTE_ALL, skipinitialspace=True):

print ("="*10 + " quoting=csv.QUOTE_ALL")
#for l in  csv.reader(lines, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
for l in  csv.reader(lines, delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
    print (l)
    for i in l:
        print (i)

print ("="*10 + " quoting=csv.QUOTE_NONE")
#for l in  csv.reader(lines, quotechar='"', delimiter=',', quoting=csv.QUOTE_NONE, skipinitialspace=True):
for l in  csv.reader(lines,  delimiter=',', quoting=csv.QUOTE_NONE, skipinitialspace=True):
    print (l)
    for i in l:
        print (i)


