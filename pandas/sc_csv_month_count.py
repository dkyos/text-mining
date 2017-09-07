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

logging.basicConfig(level=logging.DEBUG)
logging.debug('start using PhantomJS')

#np.set_printoptions(threshold=np.inf)
np.set_printoptions(threshold='nan')

print("==============================")
print(pd.describe_option('display'))
print("==============================")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print("==============================")
print(pd.describe_option('display'))
print("==============================")


tf.flags.DEFINE_string("csv", "test.csv", "CSV Filename")
FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
logging.info("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
        logging.info("{}={}".format(attr.upper(), value))
        logging.info("")

df1 = pd.read_csv(FLAGS.csv, sep='|')

df1['Category'] = df1['Process Type']
df1['date'] = pd.to_datetime(df1['Posting date'], errors='coerce')

#df1 = df[(df['date'] > '2013-01-01') & (df['date'] < '2013-12-31')]

df = pd.DataFrame({'Timestamp': df1.date, 'Category': df1.Category})

df['Month/Year'] = df['Timestamp'].apply(lambda x: "%d/%d" % (x.month, x.year) if not pd.isnull(x) else '')
print (df.groupby(['Month/Year', 'Category']).size())
#print (df.groupby(['Month/Year', 'Category']).count())


