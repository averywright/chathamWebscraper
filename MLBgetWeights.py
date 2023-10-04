import numpy as np
import ast


def relu(x):
	if x > 0:
		return x
	else:
		return 0


def deriv(x):
	if x > 0:
		return 1
	else:
		return 0


def derivativeBias(x, y, z, g, h):
	dc = z - h
	da = deriv(np.dot(x, y) + g)
	db = dc * da
	return db


def derivativeWeights(x, y, z, g, h):
	dc = z - h
	da = deriv(np.dot(x, y) + g)
	dz = x
	dw = dz * dc * da
	return dw


def back(x, y, weights, bias):
	LR = .00000005
	actual = relu(np.dot(x, weights) + bias)
	bias -= derivativeBias(x, weights, actual, bias, y)
	weights -= np.reshape(derivativeWeights(x, weights, actual, bias, y), (401, 1)) * LR

weights = np.random.rand(401,1)
counter = 0
for i in weights:
	counter += 1
	weights[counter - 1] = i /1000
bias = 1

with open ('MLBdataForTraining.txt', 'rt') as myfile:
	inputs = ast.literal_eval(myfile.read())
with open ('MLBscoresForTraining.txt', 'rt') as myfile:
	scores = ast.literal_eval((myfile.read()))

for l in range(500):
	counter = 0
	for i in inputs:
		counter += 1
		for l in i:
			try:
				for j in scores[counter-1]:
					if l == j:
						temp = []
						for k in i[l]:
							if k != '':
								temp.append(float(k))
							else:
								temp.append(0)
				 
						back(temp,float(scores[counter-1][j]),weights,bias)
			except:
			   pass
			
with open('MLBpredict.txt', 'rb+') as fh:
    fh.seek(-1, 2)
    fh.truncate()
with open("MLBweights.txt", "a") as o:
	o.write(",[")
counter = 0
for i in weights:
	counter += 1
	if counter == 1:
		with open("MLBweights.txt", "a") as o:
			o.write(str(i))
	elif counter > 1 and counter < len(weights):
		with open("MLBweights.txt", "a") as o:
			o.write(',' +str(i))
	else:
		with open("MLBweights.txt", "a") as o:
			o.write(',' + str(i) + ']]')
		

"""preDict = {}
for i in inputs[len(inputs)-1]:
	print(inputs[len(inputs) - 1][i])
	try:
		print(inputs[len(inputs)-1][i])
		temp = []
		for k in inputs[len(inputs)-1][i]:
			if k != '':
				temp.append(float(k))
			else:
				temp.append(0)
		preDict[i] = (np.dot(temp,weights)+bias, i)
	except:
		pass
	
with open("MLBpredict.txt", "a") as o:
	o.write("," + str(preDict))"""