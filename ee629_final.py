import pandas as p
import numpy as np
import datetime
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

#with open('rpidata.csv') as f:
#    data = f.readlines()
data = p.read_csv('rpidata.csv')

t = data['Date/Time']
x = data['CPU Usage %']
y = data['Temperature C']

t0 = np.array(t)
x0 = np.array(x)
y0 = np.array(y)

plt.plot(x0,y0)
plt.savefig('scatter.jpg')

print t[0]
print x[0]
print y[0]
