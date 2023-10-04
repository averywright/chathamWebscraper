import numpy as np
import random
for i in range(100):
	A = np.zeros((3, 3))
	counter = 0
	for i in A:
		counter += 1
		count = 0
		for j in i:
			count += 1
			if count == counter:
				A[counter-1, count-1] = - (random.random() ** 2)
			if count == (counter - 1):
				g = (random.random() ** 2) * random.randint(1, 20)
				A[counter - 1, count - 1] = g
				A[count-1, counter-1] = g

	
	print(A)
	print("///////")
	print(np.linalg.eig(A))
	print("///////")
