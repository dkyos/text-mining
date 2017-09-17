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
import argparse
import sc_util as sc

sc.initialize(logging.INFO)

FLAGS = None

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default='test.csv', help='input file')
FLAGS, unparsed = parser.parse_known_args()
sc.logger.info("--input [%s] " % FLAGS.input)

df_src = pd.read_csv(FLAGS.input, sep='|', error_bad_lines=False, quoting=csv.QUOTE_NONE, encoding='utf-8')

sc.logger.info('='*80)
df_mean = df_src['A3'].groupby(df_src['user'])
sc.logger.info(df_mean.mean())


sc.logger.info('='*80)
grouped = df_src.groupby('user')['A3']

def f(group):
    sc.logger.info('-'*30)
    sc.logger.info(group)
    sc.logger.info("group mean : ")
    sc.logger.info("all size : %d" % group.size)
    sc.logger.info(group.count())
    sc.logger.info(group.mean())
    return group.mean()
    #return pd.DataFrame({'original' : group, 'demeaned' : group - group.mean()})

sc.logger.info(grouped.apply(f))


