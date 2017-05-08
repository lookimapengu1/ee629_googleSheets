import pandas as p
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates

data = p.read_csv('rpidata.csv')

t = data['Date/Time']
x = data['CPU Usage %']
y = data['Temperature C']

t0 = np.array(t)
x0 = np.array(x)
x1 = range(len(x0))
y0 = np.array(y)
y1 = range(len(y0))

#Time Chart:
plt.subplot(2,1,1)
plt.plot(x1,x0,'b-')
plt.xlabel('Time (s)')
plt.ylabel('CPU Usage (%)')
plt.title('CPU Usage over Time')
frame1 = plt.gca()
frame1.axes.get_xaxis().set_visible(False)
plt.subplot(2,1,2)
plt.plot(y1,y0)
plt.xlabel('Time (s)')
plt.ylabel('CPU Temp (C)')
plt.title('CPU Temp over Time')
frame2 = plt.gca()
frame2.axes.get_xaxis().set_visible(False)
plt.savefig('timeseries.jpg')
plt.clf()


#histogram settings
num_bins = 50

#Create cpu histogram
print 'generating cpu usage histogram...'
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
plt.xlabel('CPU Usage')
plt.ylabel('Samples')
plt.title('CPU Usage Histogram')
print 'saving figure...'
plt.savefig('usehist.jpg')
print 'done with useage histogram!'
plt.clf()

#Create temp histogram
print 'generating cpu temp histogram...'
n, bins, patches = plt.hist(y, num_bins, normed=1, facecolor='green', alpha=0.5)
plt.xlabel('CPU Temp')
plt.ylabel('Samples')
plt.title('CPU Temp Histogram')
print 'saving figure...'
plt.savefig('temphist.jpg')
print 'done with temp histogram!'
plt.clf()

#Create cpu boxplot
print 'generating cpu usage boxplot...'
plt.boxplot(x0)
print 'saving figure...'
plt.savefig('usebox.jpg')
print 'done with usage boxplot!'
plt.clf()

#Create temp boxplot
print 'generating cpu temp boxplot...'
plt.boxplot(y0)
print 'saving figure...'
plt.savefig('tempbox.jpg')
print 'done with temp boxplot!'
plt.clf()

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
plt.savefig('scatter.jpg')
print 'done with scatter plot!'
