import pandas as p
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

data = p.read_csv('rpidata.csv')

t = data['Date/Time']
x = data['CPU Usage %']
y = data['Temperature C']

t0 = np.array(t)
x0 = np.array(x)
y0 = np.array(y)


#Create the scatter plot:
print 'generating scatter plot...'
scatter = plt
slope, intercept, r_value, p_value, std_err = stats.linregress(x0,y0)
l = [slope*i + intercept for i in y]
scatter.xlabel('CPU Usage (%)')
scatter.ylabel('Temperature (C)')
scatter.title('Scatter Plot')
scatter.plot(x0,y0, linestyle='None', marker='o', color='b')
scatter.plot(x0, l, 'ro')
scatter.savefig('scatter.jpg')
print 'done with scatter plot!'
