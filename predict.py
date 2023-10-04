import numpy as np
import ast
with open ('MLBdataForTraining.txt', 'rt') as myfile:
	inputs = ast.literal_eval(myfile.read())
with open ('MLBweights.txt', 'rt') as myfile:
	weights = ast.literal_eval(myfile.read())
	
bias = 1
for j in weights:
	preDict = {}
	for i in inputs[len(inputs)-1]:
		try:
			temp = []
			for k in inputs[len(inputs)-1][i]:
				if k != '':
					temp.append(float(k))
				else:
					temp.append(0)
			preDict[i] = (np.dot(temp,j)+bias)
		except:
			pass
	print(preDict)

with open('MLBpredict.txt', 'rb+') as fh:
    fh.seek(-1, 2)
    fh.truncate()
with open("MLBpredict.txt", "a") as o:
	o.write("," + str(preDict) + ']')