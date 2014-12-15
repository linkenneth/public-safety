# assume u, r, and a are properly loaded already

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
# whiskers represent +/- 2.7 std and 99.3 coverage if the data are normally
# distributed

data = [
    u['rating'],
    a['stars'],
    a[a['city'] == 'Berkeley']['stars'],
    a[a['city'] == 'Stanford']['stars'],
    a[a['city'] == 'Los Angeles']['stars'],
    r['stars'],
    r[r['city'] == 'Berkeley']['stars'],
    r[r['city'] == 'Stanford']['stars'],
    r[r['city'] == 'Los Angeles']['stars'],
]

plt.boxplot(data, vert=1, notch=True, sym='gD')

plt.xticks(range(1, 10), [
    'Near crime',
    'All businesses (all)',
    'All businesses (Berkeley)',
    'All businesses (Stanford)',
    'All businesses (LA)',
    'Restaurants (all)',
    'Restaurants (Berkeley)',
    'Restaurants (Stanford)',
    'Restaurants (LA)',
], rotation='vertical')

plt.margins(0.1)
plt.subplots_adjust(bottom=0.4)
plt.ylabel('Yelp Rating')

# plt.show()
fig.savefig('boxplot.png')
