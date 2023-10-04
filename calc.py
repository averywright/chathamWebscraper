import numpy as np
import random
a = random.randrange(-10,10)
b = random.randrange(-10,10)
c = random.randrange(-10,10)
d = random.randrange(-10,10)
e = random.randrange(-10,10)
f = random.randrange(-10,10)
g = random.randrange(-10, 10)
orig = np.array([['a', 'e', 0, 0],
	            ['e', 'b', 'f', 0],
	            [0, 'f', 'c', 'g'],
	            [0, 0 , 'g', 'd'] ])
print(orig)
try:
	print(np.linalg.inv(orig))
	print(np.linalg.det(orig))
except:
	print("error")
