#!/usr/bin/env python

### libraries
import csv
import sys
import scipy
import numpy 
import numpy as np
import matplotlib
import sklearn
import pandas
import datetime
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
import sc_util
import glob

tf.flags.DEFINE_string("output", "total.csv", "Output Filename")
FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
logging.info("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
        logging.info("{}={}".format(attr.upper(), value))
        logging.info("")

sc_util.initialize("INFO")

csv_files = glob.glob("./*.csv")
sc_util.logger.info(csv_files)

total_dataframe = pd.DataFrame() #creates a new dataframe that's empty

for name in csv_files:
    sc_util.logger.info('-'*30)
    sc_util.logger.info(name)

    df = pd.read_csv(name, sep='|')
    #total_dataframe = sc_util.append_df(total_dataframe, df)
    total_dataframe = sc_util.concat_df(total_dataframe, df)

sc_util.strip_col_name(total_dataframe)

sc_util.save_df(total_dataframe, FLAGS.output)


