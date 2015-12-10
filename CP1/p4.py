__author__ = 'Hernan Y.Ke'
import math
import matplotlib.pyplot as plt

T = range(100)
X = [(2 * math.pi * t)/len(T)for t in T]
Y = [math.sin(val) for val in X]
plt.plot(X,Y)
plt.show()