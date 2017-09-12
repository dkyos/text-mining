#!/usr/bin/env python

import csv
import sys
import scipy 
import logging 
import numpy as np 
import matplotlib 
import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm
import sklearn
import datetime
import pandas as pd
import sc_util as sc

sc.initialize(logging.INFO)

font_location = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

df = pd.read_csv('ex_histogram.csv') 

# result datafram
df_r = pd.DataFrame();

# fill NaN
df.fillna(np.nan) 
#print (df[(df.test == np.nan)])
df['test_1'] = pd.to_numeric(df['test'], errors='coerce').fillna(-1)

def set_num_min_max(x, min, max, default):
    #print ( "min:%d max:%d default:%d" % (min, max, default))
    if (x >= min) & (x <= max) :
        return x
    else:
        return default

df['test_num'] = df.test_1.map(lambda x: set_num_min_max(x, 1, 7, -1)) 
print(df['test_num'].describe())

df.test_num.hist(bins=10)
plt.show()
#df.boxplot(column='test_num')
#plt.show()
#df.boxplot(column='test_num', by='name')
#plt.show()
df.boxplot(column='test_num', by='area1', vert=False)
plt.show()

def test_normalize(x):
    ret = 0 
    if (x >= 1) & (x <= 7) :
        ret = (x/7)*5
    else:
        ret = -1
    return ret

df_r['test_normal'] = df.test_num.map(lambda x: test_normalize(x)) 
print(df_r.describe())
df_r.to_csv('result.csv', index=False)

