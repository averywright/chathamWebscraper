import matplotlib.pyplot as plt
import numpy as np

def abs(x):
	return (x**2)**.5


x = [1,2,3 ]
y = [np.log((abs(6-7.76324173) + abs(4-6.65267132) + abs(11-3.58123231) + abs(18-8.13843497))/4), np.log((abs(10 -6.9) + abs(10 - 10.63) + abs(7 - 23.17))/3), np.log((abs(12-10.33)+abs(6-6.43))/2), np.log()]
print(x, y)
plt.plot(x, y, 'ro')
plt.xlim(0,5)
plt.show()