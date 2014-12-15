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

# plt.boxplot(data, vert=1, notch=True, sym='gD')
for i in range(9):
    length = len(data[i])
    plt.scatter(i + 1 + np.random.random(length) * 0.6 - 0.3,
                data[i] + np.random.random(length) * 0.26 - 0.13,
                s=1, lw=0)

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
fig.savefig('scatter_plot.png')
