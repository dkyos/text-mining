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


tf.flags.DEFINE_string("csvfile", "test.csv", "CSV Filename")

FLAGS = tf.flags.FLAGS
FLAGS._parse_flags()
print("\nParameters:")
for attr, value in sorted(FLAGS.__flags.items()):
        print("{}={}".format(attr.upper(), value))
        print("")


df1 = pd.read_csv(FLAGS.csvfile, sep='|')

df1['Category'] = df1['Process Type']
df1['date'] = pd.to_datetime(df1['Posting date'])

df2 = df1[(df1['date'] > '2013-01-01') & (df1['date'] < '2013-12-31')]

df = pd.DataFrame({'Timestamp': df2.date, 'Category': df2.Category})

df['Month/Year'] = df['Timestamp'].apply(lambda x: "%d/%d" % (x.month, x.year))
print (df.groupby(['Month/Year', 'Category']).size())


