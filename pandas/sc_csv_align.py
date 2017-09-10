#!/usr/bin/env python

### libraries
import csv
import sys
import os
import scipy
import numpy 
import numpy as np
import matplotlib
import sklearn
import pandas
import datetime
import logging 
import pandas as pd
import tensorflow as tf
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.svm import SVR
import sc_util as sc
import glob

sc.initialize(logging.INFO)

tf.flags.DEFINE_string("indir", "./", "input directory containing csv Filenames")
tf.flags.DEFINE_string("outdir", "./", "Output directory")
FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
sc.logger.info("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
        sc.logger.info("{}={}".format(attr.upper(), value))
        sc.logger.info("")

csv_files = glob.glob(FLAGS.indir + "/*.csv")
sc.logger.info(csv_files)

total_dataframe = pd.DataFrame() #creates a new dataframe that's empty

for idx,  name in enumerate(csv_files):
    sc.logger.info(str(idx) + ' ' + '-'*30)
    sc.logger.info(name)
    
    df = pd.read_csv(name, sep='|'
        , error_bad_lines=False
        , engine='c'
        , nrows = 5
        , quoting=csv.QUOTE_NONE
        , encoding='utf-8')

    if idx == 0:
        common_columns = df.columns
    else:
        common_columns = df.columns.union(common_columns)

    sc.logger.info(common_columns)

for name in csv_files:
    sc.logger.info('-'*30)
    sc.logger.info(name)

    df = pd.read_csv(name, sep='|'
        , error_bad_lines=False
        , engine='c'
        , quoting=csv.QUOTE_NONE
        , encoding='utf-8')

    df = df.reindex(columns=common_columns)
    sc.save_df(df, FLAGS.outdir + '/' + os.path.basename(name) )



