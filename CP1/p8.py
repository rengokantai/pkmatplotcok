__author__ = 'Hernan Y.Ke'
import matplotlib.pyplot as plt

data = [5.,25.,32.]
plt.barh(range(len(data)), data, height = 1.)
plt.show()