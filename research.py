import numpy as np
import random
count = 0
div = 0
for i in range(100000):
	A = np.array([[random.randrange(-15,15),random.randrange(-15,15),random.randrange(-15,15)],[random.randrange(-15,15),random.randrange(-15,15),random.randrange(-15,15)],[random.randrange(-15,15),random.randrange(-15,15),random.randrange(-15,15)]] )
	B = np.array([[random.randrange(-15,15),random.randrange(-15,15),0],[random.randrange(-15,15),random.randrange(-15,15),random.randrange(-15,15)],[0,random.randrange(-15,15),random.randrange(-15,15)]])
	try:
		print(np.linalg.inv(A))
		print(np.linalg.inv(B))
		print("/ / / / / ")

		amag = 0
		bmag = 0
		for j in np.linalg.inv(B):
			for k in j:
				bmag += k ** 2
		for j in np.linalg.inv(A):
			for k in j:
				amag += k ** 2
		print((amag**.5) / (bmag ** .5))
		count += (amag**.5) / (bmag ** .5)
		print(count)
		div += 1
	except:
		print('e')
print(count / div)
print(div)

