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
scatter = plt
slope, intercept, r_value, p_value, std_err = stats.linregress(y0,x0)
scatter.ylabel('CPU Usage (%)')
scatter.xlabel('Temperature (C)')
scatter.title('Scatter Plot')
scatter.plot(y0,x0, linestyle='None', marker='o', color='b')
scatter.plot([intercept, intercept+slope])
scatter.savefig('scatter.jpg')

print t[0]
print x[0]
print y[0]
