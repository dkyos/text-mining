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


df = pd.read_csv("test.csv", skipinitialspace=True)

print (df)
print (df.columns)

apple_fplot = df.groupby(['Year','Fungicide'])['Value'].sum()

apple_fplot.columns = ['Year', 'Fungicide', 'Value']
print (apple_fplot)

matplotlib.style.use('ggplot')
import matplotlib.pyplot as plt

#plt.figure()
print(df.groupby(['Year','Fungicide']).sum())
print(df.groupby(['Year','Fungicide']).sum().unstack())

plot_df = df.groupby(['Year','Fungicide']).sum().unstack()
#plot_df.plot(subplots=False)
plot_df.plot(subplots=True)
plt.show()

#plot_df = apple_fplot.unstack('Fungicide').loc[:, 'Value']
#plot_df.index = pd.PeriodIndex(plot_df.index.tolist(), freq='A')
#plot_df.plot()



