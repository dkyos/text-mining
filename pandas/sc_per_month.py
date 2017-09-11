#!/usr/bin/env python

import csv
import sys
import os
import scipy
import logging
import numpy as np
import matplotlib
import sklearn
import datetime
import pandas as pd
import tensorflow as tf
import sc_util as sc
import matplotlib.pyplot as plt 

matplotlib.style.use('ggplot')

sc.initialize(logging.INFO)

tf.flags.DEFINE_string("input", "test.csv", "Input csv Filename")
FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
sc.logger.info("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
        sc.logger.info("{}={}".format(attr.upper(), value))
        sc.logger.info("")

df = pd.read_csv(FLAGS.input, sep='|', error_bad_lines=False, quoting=csv.QUOTE_NONE, encoding='utf-8')

df['Category'] = df['Process Type']
df['date'] = pd.to_datetime(df['Posting date'], errors='coerce')

df1 = pd.DataFrame({'Timestamp': df.date, 'Category': df.Category})

df1['Month/Year'] = df1['Timestamp'].apply(lambda x: "%02d/%d" % (x.month, x.year) if not pd.isnull(x) else '')
#sc.logger.info(df1.groupby(['Month/Year', 'Category']).size().unstack()

df2 = df1.groupby(['Month/Year', 'Category']).size()
sc.logger.info(df2)
plot_df = df2.unstack()
sc.logger.info(plot_df)
plot_df.plot(subplots=True)
plt.savefig(os.path.basename(FLAGS.input) + '.png')
#plt.show()
