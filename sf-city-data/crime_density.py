#!/usr/bin/python

import numpy as np
import pandas as pd
import scipy.stats as stats

DATA_PATH = './sfpd-reported-incidents-2003-to-present'
NAME_F = 'sfpd_incident_%d.csv'
YEARS = range(2003, 2014 + 1)  # 2003 to 2014, inclusive

data = {}
for year in YEARS:
    name = NAME_F % year
    data[year] = pd.read_csv('%s/%s' % (DATA_PATH, name))

geo = data[2014][['X', 'Y']]
geo_array = geo.values.T

density = stats.gaussian_kde(geo_array)
xmin = geo_array[0].min()
xmax = geo_array[0].max()
ymin = geo_array[1].min()
ymax = geo_array[1].max()

mgrid = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
other = []
for i in xrange(100):
    other.append([])
    for j in xrange(100):
        coords = (mgrid[0][i][j], mgrid[1][i][j])
        other[i].append(density(coords)[0])
