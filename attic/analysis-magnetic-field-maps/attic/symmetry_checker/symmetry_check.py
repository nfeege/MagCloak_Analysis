import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

M = np.genfromtxt('data/DataFile_141118_122119.txt')

zero = 151

x = M[:,0]-zero
y = M[:,1]

positive = np.where(x>0)
negative = np.where(x<0)

#plt.plot(x,y)
plt.plot(-x[negative], y[negative], marker = '.', label = 'z < 0')
plt.plot(x[positive], y[positive], marker = '.', label = 'z > 0')
plt.xlabel('|z| [mm]')
plt.ylabel('By [mT]')
plt.title('5 Layers, Cu Stabilizer, SC Cap')
plt.legend(loc = 'best')

plt.savefig('fringe_study.png')
plt.close()
