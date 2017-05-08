import pandas as p
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

data = p.read_csv('rpidata.csv')

for line in data:
    if data['Date/Time'].empty: print "uh oh"

t = data['Date/Time']
x = data['CPU Usage %']
y = data['Temperature C']

t0 = np.array(t)
x0 = np.array(x)
y0 = np.array(y)

#histogram settings
num_bins = 50

#Create cpu histogram
print 'generating cpu usage histogram'
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
plt.xlabel('CPU Usage')
plt.ylabel('Samples')
plt.title('CPU Usage Histogram')
#plt.plot(bins, x0, 'r--')
print 'saving figure...'
plt.savefig('usehist.jpg')
print 'done with useage histogram!'
plt.clf

#Create the scatter plot:
print 'generating scatter plot...'
slope, intercept, r_value, p_value, std_err = stats.linregress(x0,y0)
l = [slope*i + intercept for i in x0]
plt.xlabel('CPU Usage (%)')
plt.ylabel('Temperature (C)')
plt.title('Scatter Plot')
plt.plot(x0,y0, linestyle='None', marker='o', color='b')
plt.plot(x0, l, 'r-')
print 'saving figure...'
plt.savefig('scatter1.jpg')
print 'done with scatter plot!'
