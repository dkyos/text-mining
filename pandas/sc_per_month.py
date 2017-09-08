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

tf.flags.DEFINE_string("input", "test.csv", "Input csv Filename")
FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
sc_util.logger.info("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
        sc_util.logger.info("{}={}".format(attr.upper(), value))
        sc_util.logger.info("")

df = pd.read_csv(FLAGS.input, sep='|', error_bad_lines=False, quoting=csv.QUOTE_NONE, encoding='utf-8')

df['Category'] = df['Process Type']
df['date'] = pd.to_datetime(df['Posting date'], errors='coerce')

df1 = pd.DataFrame({'Timestamp': df.date, 'Category': df.Category})

df1['Month/Year'] = df1['Timestamp'].apply(lambda x: "%d/%d" % (x.month, x.year) if not pd.isnull(x) else '')
sc_util.logger.info(df1.groupby(['Month/Year', 'Category']).size())
#print (df1.groupby(['Month/Year', 'Category']).count())


