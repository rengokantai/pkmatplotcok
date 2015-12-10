__author__ = 'Hernan Y.Ke'

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('spdata.txt')

plt.plot(data[:,0],data[:,1])
plt.show()