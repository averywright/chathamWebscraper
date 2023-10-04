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
print(np.linalg.det(A))


def inv(x):
	count = 0
	for i in x:
		count += 1
		try:
			x[count, count] = x[count, count] - (x[count - 1, count] * x[count, count - 1] / x[count - 1, count - 1])
			x[count, count-1] = 0
		except:
			error = True
	count = 0
	det = 1
	for i in x:
		count += 1
		counter = 0
		for j in i:
			counter += 1
			if counter == count:
				det = det * A[counter - 1, counter -1]
	return det

print(det)
print(A)


