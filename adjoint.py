import numpy as np
import random
A = np.zeros((9, 9))
counter = 0
for i in A:
	counter += 1
	count = 0
	for j in i:
		count += 1
		if count == counter:
			A[counter-1, count-1] = random.random()
		if count == counter -1:
			A[counter - 1, count - 1] = random.random()
		if counter == count-1:
			A[counter - 1, count - 1] = random.random()
print(A)
adjoint = np.zeros((9, 9))
counter = 0
for i in A:
	counter += 1
	count = 0
	for j in i:
		count += 1
		x = np.zeros((8, 8))
		counterTwo = 0
		one = False
		for k in A:
			counterTwo += 1
			if counterTwo == counter:
				one = True
				pass
			countTwo = 0
			two = False
			for l in k:
				countTwo += 1
				if countTwo == count:
					two = True
					pass
				if one and two:
					x[counterTwo - 2, countTwo - 2] = l
				if one and not two:
					x[counterTwo - 2, countTwo - 1] = l
				if two and not one:
					x[counterTwo - 1, countTwo - 2] = l
				if not one and not two:
					x[counterTwo-1, countTwo-1] = l
		
		g = 1
		if (counter + count) % 2 != 0:
			g = -1
		adjoint[counter - 1, count -1] = np.linalg.det(x) * g
print(adjoint * 1/ np.linalg.det(A))



