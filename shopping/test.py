#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


import matplotlib
print(matplotlib.get_backend())

matplotlib.rcParams['backend'] = 'TkAgg' 

print(matplotlib.get_backend())


import matplotlib
matplotlib.use('TkAgg') 


import matplotlib
matplotlib.rcParams['backend'] = "Qt4Agg"


fig = plt.figure()
plt.show()

import pylab
pylab.show()
