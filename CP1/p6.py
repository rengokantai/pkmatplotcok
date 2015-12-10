__author__ = 'Hernan Y.Ke'

import matplotlib.pyplot as plt

with open('spdata.txt','r') as f:
    x,y = zip(*[[float(s) for s in line.split()] for line in f])

plt.plot(x,y)
plt.show()