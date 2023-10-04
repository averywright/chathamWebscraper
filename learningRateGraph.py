import numpy as np
import random
import math


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


weights = np.random.rand(45, 1)
counter = 0
for i in weights:
	counter += 1
	g = random.randint(0, 1)
	weights[counter - 1] += 1
	if g == 1:
		weights[counter - 1] = weights[counter - 1] * -1

bias = 10

brewersRuns = np.array(
	[.20, .12, .1, .497, .32, .1189, .1055, .159, .250, .55, .4, .43, .152, .20, .9, .109, .292, .237, .315, .419,
	 .734,
	 .20, .17, .982, .297, .360, .186, .234, .248, .482, .247, 0.7, .256, .58, .863, .319, .234, .479, .234, 0.92, .13,
	 0.7, .123, 0, .65 - 1.28977])
marlinsRuns = np.array(
	[14, 17, 4, 4.13, 31, 1169, 1041, 128, 248, 44, 7, 30, 123, 16, 5, 101, 276, .238, .314, .380, .695, 18, 27, .984,
	 29.5, 38.2, .170, .226, .311, .537, .222, 3.4, 34.3, 5.5, 90.4, 46.4, 19.8, 47.7, 30.2, 0.91, 1.1, 0.7, 11.2, 1,
	 6.5 - 12.8977])

redsRuns = np.array(
	[8, 24, 5, 4.13, 32, 1161, 1035, 132, 226, 55, 2, 26, 128, 11, 6, 96, 300, .218, .293, .351, .644, 12, 23, .989,
	 30.0, 28.0, .284, .346, .422, .769, .330, 3.2, 18.9, 7.9, 85.8, 30.8, 20.7, 48.9, 20.7, 0.98, -0.6, -0.3, -5.3, 0,
	 8 - 1.07016])
piratesRuns = np.array(
	[13, 18, 3, 3.65, 31, 1139, 1020, 113, 240, 43, 7, 25, 104, 11, 6, 103, 270, .235, .306, .365, .671, 27, 20, .975,
	 27.6, 30.2, .256, .345, .397, .742, .330, 1.4, 23.0, 12.2, 88.5, 36.7, 22.2, 34.4, 33.3, 0.53, -0.3, -0.1,
	 -5.3, 1,
	 8 - 1.07016])

astrosRuns = np.array(
	[21, 11, 1, 4.09, 32, 1195, 1055, 131, 236, 51, 3, 40, 128, 14, 6, 123, 259, .224, .306, .391, .697, 12, 28, .989,
	 29.6, 31.1, .219, .321, .412, .733, .267, 3.8, 26.0, 12.2, 89.9, 43.0, 31.3, 25.0, 30.0, 0.34, 0.1, 0.2, 2.8, 0,
	 (8 - 5.01496212)])
nationalsRuns = np.array(
	[11, 22, 5, 4.12, 33, 1223, 1101, 136, 278, 54, 1, 24, 130, 10, 5, 96, 244, .252, .317, .369, .685, 26, 21, .978,
	 29.6, 32.1, .227, .326, .294, .620, .280, 0.7, 18.8, 10.9, 87.8, 33.0, 22.3, 71.3, 4.3, 2.58, 0.5, 0.3, 5.7, 1,
	 (8 - 5.01496212)])

counter = 0
for i in brewersRuns:
	counter += 1
	if i > 1 and i < 10:
		brewersRuns[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 < 100:
		brewersRuns[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		brewersRuns[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		brewersRuns[counter - 1] = i / 10000
counter = 0
for i in marlinsRuns:
	counter += 1
	if i > 1 and i < 10:
		marlinsRuns[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 < 100:
		marlinsRuns[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		marlinsRuns[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		marlinsRuns[counter - 1] = i / 10000
counter = 0
for i in astrosRuns:
	counter += 1
	if i > 1 and i < 10:
		astrosRuns[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 < 100:
		astrosRuns[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		astrosRuns[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		astrosRuns[counter - 1] = i / 10000
counter = 0
for i in redsRuns:
	counter += 1
	if i > 1 and i < 10:
		redsRuns[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 < 100:
		redsRuns[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		redsRuns[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		redsRuns[counter - 1] = i / 10000
counter = 0
for i in piratesRuns:
	counter += 1
	if i > 1 and i < 10:
		piratesRuns[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 < 100:
		piratesRuns[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		piratesRuns[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		piratesRuns[counter - 1] = i / 10000
counter = 0
for i in nationalsRuns:
	counter += 1
	if i > 1 and i < 10:
		nationalsRuns[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 < 100:
		nationalsRuns[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		nationalsRuns[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		nationalsRuns[counter - 1] = i / 10000

marlinsRuns2 = np.array(
	[15, 18, 4, 4.18, 33, 1238, 1107, 138, 264, 46, 7, 34, 132, 17, 6, 105, 294, .238, .313, .385, .697, 18, 28, .985,
	 29.5, 28.2, .261, .331, .432, .763, .352, 3.2, 29.4, 7.9, 87.9, 46.1, 23.7, 38.2, 27.6, 0.63, -0.1, -0.1, -1.2, 0,
	 3.972014256666665])
counter = 0
for i in marlinsRuns2:
	counter += 1
	if i > 1 and i < 10:
		marlinsRuns2[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 < 100:
		marlinsRuns2[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		marlinsRuns2[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		marlinsRuns2[counter - 1] = i / 10000

nationalsRuns3 = np.array(
	[12, 24, 5, 4.17, 36, 1336, 1202, 150, 304, 57, 1, 26, 143, 10, 5, 107, 267, .253, .318, .367, .685, 27, 25, .979,
	 29.6, 42.2, .221, .316, .356, .671, .266, 2.3, 21.6, 11.1, 85.4, 34.8, 20.4, 48.7, 19.5, 0.98, 1.0, 0.5, 6.8, 0,
	 -0.3973856211111109])
marlinsRuns3 = np.array(
	[15, 19, 4, 4.15, 34, 1275, 1141, 141, 269, 48, 7, 35, 135, 17, 6, 107, 308, .236, .309, .382, .691, 20, 29, .984,
	 29.5, 19.0, .316, .341, .487, .828, .323, 3.7, 12.2, 3.7, 92.9, 58.2, 17.6, 48.5, 26.5, 1.06, -0.6, -0.2, -5.3, 1,
	 -0.3973856211111109])

tigersRuns3 = np.array(
	[12, 23, 5, 2.86, 35, 1249, 1129, 100, 254, 46, 5, 16, 98, 5, 5, 99, 290, .225, .292, .317, .609, 20, 24, .984,
	 28.9, 29.2, .282, .320, .436, .756, .333, 3.2, 21.6, 4.8, 88.6, 39.6, 24.2, 41.8, 27.5, 0.72, 0.1, 0.0, -0.6, 0,
	 -0.1714285699999998])
raysRuns3 = np.array(
	[21, 14, 2, 4.17, 35, 1284, 1163, 146, 272, 55, 8, 31, 135, 29, 9, 103, 306, .234, .301, .375, .676, 19, 19, .985,
	 27.0, 10.0, .308, .349, .462, .810, .355, 2.3, 18.6, 7.0, 89.8, 40.6, 21.9, 43.8, 21.9, 0.82, 0.0, 0.0, 1.0, 1,
	 -0.1714285699999998])

yankeesRuns3 = np.array(
	[25, 9, 1, 4.91, 34, 1274, 1118, 167, 271, 47, 2, 49, 158, 21, 7, 126, 286, .242, .323, .419, .742, 13, 22, .990,
	 30.7, 17.0, .254, .297, .441, .738, .293, 4.7, 25.0, 4.7, 92.9, 45.5, 20.5, 43.2, 31.8, 0.76, 0.2, 0.1, -0.3, 0,
	 -1.919981328888889])
oriolesRuns3 = np.array(
	[14, 21, 4, 3.26, 35, 1304, 1165, 114, 266, 54, 3, 25, 109, 20, 6, 104, 319, .228, .302, .344, .647, 25, 45, .980,
	 28.1, 28.2, .259, .320, .438, .757, .325, 3.2, 25.0, 7.3, 84.8, 38.6, 24.1, 44.6, 21.7, 0.84, 0.2, 0.1, 0.9, 1,
	 -1.919981328888889])

marinersRuns3 = np.array(
	[15, 19, 4, 4.15, 34, 1275, 1141, 141, 269, 48, 7, 35, 135, 17, 6, 107, 308, .236, .309, .382, .691, 20, 29, .984,
	 29.5, 26.0, .211, .327, .432, .759, .246, 3.5, 23.7, 14.9, 92.0, 50.0, 21.4, 51.4, 21.4, 1.09, 0.0, 0.0, -0.6, 0,
	 3.141269845555554])
blueJaysRuns3 = np.array(
	[18, 17, 3, 3.71, 35, 1272, 1149, 130, 268, 57, 0, 37, 129, 15, 6, 91, 289, .233, .296, .379, .675, 16, 21, .987,
	 27.0, 34.0, .258, .309, .430, .739, .275, 3.6, 15.7, 7.1, 90.1, 45.8, 20.4, 38.9, 33.3, 0.67, 0.2, 0.2, 2.3, 1,
	 3.141269845555554])

astrosRuns3 = np.array(
	[23, 12, 1, 4.31, 35, 1315, 1163, 151, 266, 56, 4, 48, 147, 16, 6, 132, 284, .229, .309, .408, .717, 12, 30, .990,
	 29.7, 24.2, .169, .235, .303, .538, .226, 3.1, 34.7, 8.2, 91.5, 40.0, 17.9, 39.3, 28.6, 0.65, 0.8, 0.5, 6.3, 0,
	 -0.3464985966666685])
redSoxRuns3 = np.array(
	[13, 21, 5, 3.71, 34, 1276, 1154, 126, 271, 73, 2, 20, 125, 7, 5, 86, 281, .235, .290, .354, .644, 16, 23, .987,
	 28.9, 26.2, .229, .315, .302, .617, .269, 0.9, 15.6, 10.1, 87.4, 31.3, 27.5, 33.8, 23.8, 0.52, 0.4, 0.3, 3.3, 1,
	 -0.3464985966666685])

cardinalsRuns3 = np.array(
	[19, 15, 2, 4.62, 34, 1272, 1134, 157, 279, 61, 4, 32, 152, 29, 3, 110, 244, .246, .319, .392, .711, 15, 36, .988,
	 29.4, 11.0, .327, .353, .429, .782, .385, 1.9, 17.3, 3.9, 83.7, 36.6, 29.3, 39.0, 17.1, 0.73, -0.8, -0.5, -4.9, 0,
	 4.128758166666664])
metsRuns3 = np.array(
	[23, 13, 1, 4.44, 36, 1365, 1203, 160, 302, 56, 7, 29, 149, 15, 7, 121, 275, .251, .329, .382, .711, 12, 26, .991,
	 30.1, 42.1, .206, .253, .277, .530, .244, 1.2, 18.7, 4.8, 86.5, 28.5, 20.0, 50.4, 24.0, 1.02, 1.1, 0.8, 13.2, 1,
	 4.128758166666664])

bravesRuns3 = np.array(
	[16, 19, 3, 4.17, 35, 1291, 1151, 146, 262, 61, 1, 44, 137, 17, 2, 114, 334, .228, .302, .397, .699, 18, 22, .985,
	 28.6, 28.2, .231, .315, .343, .657, .338, 0.8, 30.7, 8.9, 87.5, 47.2, 29.2, 43.1, 20.8, 0.76, 0.2, 0.2, -0.3, 0,
	 2.034920637777777])
brewersRuns3 = np.array(
	[22, 13, 1, 4.89, 35, 1303, 1158, 171, 273, 57, 4, 49, 164, 24, 9, 116, 323, .236, .312, .419, .731, 22, 18, .982,
	 29.7, 30.0, .230, .326, .416, .742, .253, 3.1, 17.1, 12.4, 90.0, 42.9, 25.3, 48.4, 15.4, 0.94, 0.3, 0.1, 1.2, 1,
	 2.034920637777777])

piratesRuns3 = np.array(
	[15, 19, 3, 3.50, 34, 1234, 1105, 119, 252, 45, 7, 27, 109, 11, 6, 113, 298, .228, .300, .355, .655, 27, 23, .978,
	 27.6, 3.0, .385, .556, .385, .940, .417, 0.0, 5.6, 27.8, 87.5, 41.7, 8.3, 83.3, 0.0, 5.00, -0.2, -0.1, -1.6, 0,
	 2.361616162222225])
cubsRuns3 = np.array(
	[13, 20, 4, 3.94, 33, 1210, 1079, 130, 250, 54, 5, 25, 117, 10, 9, 108, 298, .232, .309, .361, .670, 19, 38, .984,
	 28.7, 19.2, .082, .200, .082, .282, .109, 0.0, 21.4, 12.9, 85.9, 31.1, 23.9, 45.7, 23.9, 0.84, 0.5, 0.3, 7.1, 1,
	 2.361616162222225])

angelsRuns3 = np.array(
	[24, 13, 1, 4.92, 37, 1380, 1228, 182, 302, 58, 5, 49, 176, 22, 12, 129, 337, .246, .321, .421, .742, 19, 33, .986,
	 28.5, 16.1, .220, .309, .339, .648, .256, 2.9, 22.1, 10.3, 87.4, 37.8, 22.2, 48.9, 20.0, 1.00, -0.1, -0.1,
	 -1.8, 0,
	 -0.4447174433333352])
rangersRuns3 = np.array(
	[14, 19, 4, 3.97, 33, 1199, 1088, 131, 234, 35, 3, 33, 122, 24, 8, 95, 259, .215, .281, .344, .625, 23, 26, .981,
	 29.3, 29.1, .227, .275, .318, .593, .258, 1.7, 17.5, 5.0, 87.1, 36.7, 19.8, 49.5, 23.1, 0.98, 0.7, 0.4, 6.9, 1,
	 -0.4447174433333352])

giantsRuns3 = np.array(
	[20, 13, 3, 4.94, 33, 1254, 1092, 163, 268, 43, 2, 33, 153, 20, 6, 128, 267, .245, .329, .379, .708, 16, 29, .987,
	 30.1, 27.2, .402, .433, .538, .972, .413, 1.6, 6.2, 5.4, 90.1, 43.2, 35.4, 41.6, 16.8, 0.75, -0.4, -0.3, -4.2, 0,
	 0.3653594788888892])
rockiesRuns3 = np.array(
	[17, 16, 5, 4.64, 33, 1236, 1111, 153, 289, 59, 6, 33, 143, 7, 7, 96, 260, .260, .325, .413, .738, 26, 45, .979,
	 29.6, 30.0, .274, .331, .419, .750, .337, 3.1, 23.4, 7.0, 87.5, 40.2, 27.3, 48.9, 21.6, 0.98, 0.1, 0.0, 0.7, 1,
	 0.3653594788888892])

twinsRuns3 = np.array(
	[19, 15, 1, 3.94, 34, 1245, 1106, 134, 266, 60, 1, 35, 126, 6, 6, 113, 293, .241, .318, .392, .709, 17, 24, .986,
	 27.0, 13.1, .216, .259, .392, .651, .243, 3.7, 22.2, 5.6, 89.7, 43.6, 15.4, 28.2, 38.5, 0.39, 0.2, 0.0, 4.1, 0,
	 -3.321750323333333])
athleticsRuns3 = np.array(
	[15, 21, 4, 3.36, 36, 1273, 1149, 121, 231, 49, 6, 22, 112, 22, 5, 99, 318, .201, .269, .312, .580, 25, 36, .981,
	 28.7, 22.1, .241, .330, .506, .836, .250, 6.0, 22.0, 12.0, 89.3, 45.5, 27.3, 34.8, 31.8, 0.53, -0.3, -0.2,
	 -1.7, 1,
	 -3.321750323333333])

counter = 0
for i in marlinsRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		marlinsRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		marlinsRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		marlinsRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		marlinsRuns3[counter - 1] = i / 10000

counter = 0
for i in nationalsRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		nationalsRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		nationalsRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		nationalsRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		nationalsRuns3[counter - 1] = i / 10000
counter = 0
for i in athleticsRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		athleticsRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		athleticsRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		athleticsRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		athleticsRuns3[counter - 1] = i / 10000

counter = 0
for i in twinsRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		twinsRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		twinsRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		twinsRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		twinsRuns3[counter - 1] = i / 10000
counter = 0
for i in giantsRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		giantsRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		giantsRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		giantsRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		giantsRuns3[counter - 1] = i / 10000

counter = 0
for i in rockiesRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		rockiesRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		rockiesRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		rockiesRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		rockiesRuns3[counter - 1] = i / 10000

counter = 0
for i in rangersRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		rangersRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		rangersRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		rangersRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		rangersRuns3[counter - 1] = i / 10000

counter = 0
for i in cardinalsRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		cardinalsRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		cardinalsRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		cardinalsRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		cardinalsRuns3[counter - 1] = i / 10000

counter = 0
for i in brewersRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		brewersRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		brewersRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		brewersRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		brewersRuns3[counter - 1] = i / 10000
counter = 0
for i in cubsRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		cubsRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		cubsRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		cubsRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		cubsRuns3[counter - 1] = i / 10000

counter = 0
for i in angelsRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		angelsRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		angelsRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		angelsRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		angelsRuns3[counter - 1] = i / 10000

counter = 0
for i in raysRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		raysRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		raysRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		raysRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		raysRuns3[counter - 1] = i / 10000

counter = 0
for i in metsRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		metsRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		metsRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		metsRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		metsRuns3[counter - 1] = i / 10000
counter = 0
for i in piratesRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		piratesRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		piratesRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		piratesRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		piratesRuns3[counter - 1] = i / 10000

counter = 0
for i in astrosRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		astrosRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		astrosRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		astrosRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		astrosRuns3[counter - 1] = i / 10000
counter = 0
for i in bravesRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		bravesRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		bravesRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		bravesRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		bravesRuns3[counter - 1] = i / 10000

counter = 0
for i in blueJaysRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		blueJaysRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		blueJaysRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		blueJaysRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		blueJaysRuns3[counter - 1] = i / 10000

counter = 0
for i in redSoxRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		redSoxRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		redSoxRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		redSoxRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		redSoxRuns3[counter - 1] = i / 10000

counter = 0
for i in marinersRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		marinersRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		marinersRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		marinersRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		marinersRuns3[counter - 1] = i / 10000
counter = 0
for i in yankeesRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		yankeesRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		yankeesRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		yankeesRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		yankeesRuns3[counter - 1] = i / 10000

counter = 0
for i in tigersRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		tigersRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		tigersRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 <= 1000:
		tigersRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 >= 1000 and (i ** 2) ** .5 <= 10000:
		tigersRuns3[counter - 1] = i / 10000

counter = 0
for i in oriolesRuns3:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		oriolesRuns3[counter - 1] = i / 10
	elif (i ** 2) ** .5 > 10 and (i ** 2) ** .5 <= 100:
		oriolesRuns3[counter - 1] = i / 100
	elif (i ** 2) ** .5 > 100 and (i ** 2) ** .5 < 1000:
		oriolesRuns3[counter - 1] = i / 1000
	elif (i ** 2) ** .5 > 1000 and (i ** 2) ** .5 <= 10000:
		oriolesRuns3[counter - 1] = i / 10000

reds = np.array(
	[9, 26, 5, 4.03, 35, 1267, 1130, 141, 244, 61, 2, 29, 137, 14, 6, 106, 318, .216, .291, .350, .641, 12, 25, .990,
	 30.0, 32.2, .260, .315, .435, .750, .271, 3.5, 14.0, 7.0, 90.0, 44.1, 26.8, 37.5, 31.3, 0.61, -0.2, -0.1, -2.1, 0,
	 -4.524963921111111])
guardians = np.array(
	[16, 17, 3, 4.76, 33, 1257, 1131, 157, 284, 58, 9, 31, 154, 18, 6, 104, 250, .251, .317, .401, .717, 18, 20, .985,
	 26.2, 17.0, .214, .290, .250, .540, .250, 0.0, 12.9, 9.7, 93.1, 52.1, 25.0, 45.8, 20.8, 0.85, 0.7, 0.1, 6.7, 1,
	 -4.524963921111111])

nationals = np.array(
	[12, 25, 5, 4.11, 37, 1373, 1235, 152, 309, 57, 1, 26, 145, 11, 5, 108, 273, .250, .315, .361, .676, 29, 28, .978,
	 29.6, 16.1, .161, .254, .214, .468, .214, 0.0, 22.2, 11.1, 91.8, 42.9, 21.4, 54.8, 23.8, 1.21, 0.1, 0.0, 4.3, 0,
	 0.8208065255555557])
marlins = np.array(
	[16, 19, 3, 4.26, 35, 1313, 1177, 149, 285, 53, 7, 36, 142, 17, 7, 110, 314, .242, .315, .391, .705, 21, 29, .983,
	 29.5, 32.0, .260, .391, .439, .830, .308, 2.7, 19.2, 15.2, 88.0, 37.9, 25.3, 43.2, 28.4, 0.79, -0.9, -0.3,
	 -8.0, 1,
	 0.8208065255555557])

padres = np.array(
	[22, 13, 2, 4.57, 35, 1332, 1154, 160, 263, 53, 7, 30, 155, 15, 6, 138, 299, .228, .316, .364, .680, 13, 28, .990,
	 28.5, 24.0, .274, .314, .400, .714, .325, 1.0, 17.7, 4.9, 82.8, 27.3, 21.8, 46.2, 25.6, 0.86, -0.3, -0.2, -0.9, 0,
	 0.8412698455555567])
phillies = np.array(
	[17, 18, 2, 4.91, 35, 1313, 1181, 172, 302, 63, 6, 44, 163, 24, 3, 105, 306, .256, .319, .431, .750, 20, 29, .984,
	 28.9, 9.0, .270, .357, .378, .736, .346, 2.4, 23.8, 11.9, 87.0, 30.8, 14.8, 48.1, 29.6, 0.93, 0.1, 0.0, 0.7, 1,
	 0.8412698455555567])

yankees = np.array(
	[26, 9, 1, 4.94, 35, 1317, 1155, 173, 282, 48, 2, 52, 164, 21, 7, 131, 296, .244, .325, .424, .749, 14, 24, .989,
	 30.7, 26.0, .279, .364, .500, .864, .287, 3.4, 11.0, 10.2, 91.4, 42.9, 22.0, 48.4, 24.2, 0.94, -0.4, -0.1,
	 -5.0, 0,
	 -2.090476185555556])
orioles = np.array(
	[14, 22, 5, 3.22, 36, 1336, 1194, 116, 269, 54, 3, 27, 111, 20, 6, 106, 330, .225, .300, .343, .643, 25, 45, .981,
	 28.1, 26.0, .279, .364, .500, .864, .287, 3.4, 11.0, 10.2, 91.4, 42.9, 22.0, 48.4, 24.2, 0.94, -0.4, -0.1,
	 -5.0, 1,
	 -2.090476185555556])

mariners = np.array(
	[16, 20, 3, 3.92, 36, 1357, 1196, 141, 277, 50, 6, 35, 136, 18, 8, 134, 299, .232, .316, .371, .687, 19, 28, .985,
	 26.9, 34.0, .292, .350, .479, .829, .316, 3.8, 15.3, 7.0, 91.1, 49.2, 34.2, 30.0, 28.3, 0.43, -0.3, 0.0, -1.8, 0,
	 3.649999995555554])
blueJays = np.array(
	[19, 17, 3, 3.78, 36, 1311, 1182, 136, 278, 57, 0, 39, 135, 15, 6, 96, 299, .235, .299, .382, .681, 17, 21, .987,
	 27.0, 38.0, .203, .281, .283, .564, .269, 2.0, 27.5, 9.2, 90.0, 46.9, 31.3, 36.5, 24.0, 0.57, 0.7, 0.5, 7.8, 1,
	 3.649999995555554])

counter = 0
for i in blueJays:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		blueJays[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		blueJays[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		blueJays[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		blueJays[counter - 1] = i / 10000

counter = 0
for i in mariners:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		mariners[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		mariners[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		mariners[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		mariners[counter - 1] = i / 10000

counter = 0
for i in orioles:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		orioles[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		orioles[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		orioles[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		orioles[counter - 1] = i / 10000
counter = 0
for i in yankees:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		yankees[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		yankees[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		yankees[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		yankees[counter - 1] = i / 10000

counter = 0
for i in phillies:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		phillies[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		phillies[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		phillies[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		phillies[counter - 1] = i / 10000

counter = 0
for i in padres:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		padres[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		padres[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		padres[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		padres[counter - 1] = i / 10000

counter = 0
for i in marlins:
	marlins += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		marlins[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		marlins[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		marlins[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		marlins[counter - 1] = i / 10000
counter = 0
for i in nationals:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		nationals[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		nationals[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		nationals[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		nationals[counter - 1] = i / 10000

counter = 0
for i in guardians:
	guardians += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		guardians[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		guardians[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		guardians[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		guardians[counter - 1] = i / 10000
counter = 0
for i in reds:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		reds[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		reds[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		reds[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		reds[counter - 1] = i / 10000

twins2 = np.array(
	[21, 16, 1, 3.84, 37, 1350, 1202, 142, 285, 63, 1, 40, 134, 7, 6, 121, 314, .237, .313, .391, .704, 17, 26, .987,
	 27.0, 35.1, .275, .307, .430, .736, .302, 2.7, 15.3, 3.3, 88.9, 38.7, 24.2, 45.0, 25.8, 0.83, -0.5, -0.2, -2.8, 0,
	 -1.86])
athletics2 = np.array(
	[16, 23, 5, 3.28, 39, 1382, 1242, 128, 251, 54, 6, 23, 119, 24, 5, 109, 334, .202, .272, .311, .583, 28, 36, .980,
	 28.7, 14.2, .204, .317, .389, .706, .258, 4.8, 31.8, 14.3, 89.8, 41.2, 11.8, 50.0, 23.5, 1.00, 0.0, 0.0, 0.7, 1,
	 -1.86])

yankees2 = np.array(
	[27, 9, 1, 4.94, 36, 1359, 1192, 178, 293, 52, 2, 54, 168, 21, 7, 135, 299, .246, .327, .429, .756, 15, 25, .989,
	 30.7, 39.0, .294, .358, .464, .822, .336, 2.9, 18.5, 8.1, 89.3, 41.1, 25.8, 42.7, 22.6, 0.77, -0.1, -0.1, -1.5, 0,
	 -1.73])
orioles2 = np.array(
	[14, 23, 5, 3.24, 37, 1373, 1229, 120, 278, 57, 3, 28, 115, 21, 6, 107, 339, .226, .299, .346, .645, 26, 46, .981,
	 28.1, 36.2, .210, .276, .362, .639, .273, 3.3, 30.3, 7.9, 89.7, 43.5, 24.7, 44.1, 26.9, 0.79, 0.5, 0.4, 6.5, 1,
	 -1.73])

whiteSox2 = np.array(
	[18, 18, 2, 3.50, 36, 1306, 1192, 126, 270, 51, 1, 32, 118, 19, 1, 81, 259, .227, .283, .352, .634, 27, 30, .979,
	 29.4, 38.1, .282, .297, .376, .673, .292, 1.3, 8.9, 1.9, 88.3, 42.4, 28.1, 37.4, 23.0, 0.60, 0.2, 0.2, 2.5, 0,
	 1.77])
royals2 = np.array(
	[13, 22, 4, 3.51, 35, 1293, 1173, 123, 264, 49, 8, 22, 113, 20, 6, 100, 266, .225, .290, .337, .626, 14, 36, .989,
	 28.8, 26.2, .221, .286, .421, .707, .296, 4.8, 35.2, 8.6, 87.8, 40.7, 25.4, 32.2, 37.3, 0.48, 0.7, 0.3, 5.7, 1,
	 1.77])

diamondbacks2 = np.array(
	[18, 20, 4, 3.61, 38, 1383, 1219, 137, 250, 54, 5, 41, 128, 16, 9, 138, 352, .205, .290, .358, .649, 31, 33, .977,
	 27.3, 41.2, .244, .297, .350, .647, .295, 1.7, 20.4, 5.8, 87.6, 42.6, 25.6, 44.0, 21.6, 0.80, 0.7, 0.4, 8.6, 0,
	 -4.21])
dodgers2 = np.array(
	[24, 12, 1, 5.50, 36, 1366, 1192, 198, 291, 71, 7, 38, 182, 19, 4, 154, 289, .244, .332, .411, .743, 19, 33, .985,
	 29.7, 35.1, .213, .290, .331, .620, .242, 2.1, 19.3, 10.3, 84.6, 29.4, 21.6, 47.1, 21.6, 0.91, 0.1, 0.1, 0.3, 1,
	 -4.21])

tigers2 = np.array(
	[13, 24, 5, 2.81, 37, 1317, 1195, 104, 267, 46, 5, 19, 102, 5, 5, 99, 308, .223, .288, .318, .606, 21, 26, .984,
	 29.0, 33.2, .185, .241, .282, .523, .221, 1.5, 20.3, 6.0, 90.4, 45.3, 22.7, 49.5, 20.6, 0.98, 0.7, 0.4, 6.4, 0,
	 -2.01])
rays2 = np.array(
	[22, 15, 2, 4.22, 37, 1355, 1227, 156, 290, 58, 8, 35, 145, 29, 10, 107, 316, .236, .302, .382, .684, 20, 21, .985,
	 27.1, 38.2, .214, .286, .366, .651, .250, 2.5, 21.0, 9.3, 86.9, 35.4, 21.2, 37.2, 32.7, 0.60, -0.2, -0.2, -2.9, 1,
	 -2.01])

counter = 0
for i in twins2:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		twins2[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		twins2[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		twins2[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		twins2[counter - 1] = i / 10000

counter = 0
for i in athletics2:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		athletics2[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		athletics2[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		athletics2[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		athletics2[counter - 1] = i / 10000

counter = 0
for i in yankees2:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		yankees2[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		yankees2[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		yankees2[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		yankees2[counter - 1] = i / 10000
counter = 0
for i in orioles2:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		orioles2[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		orioles2[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		orioles2[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		orioles2[counter - 1] = i / 10000

counter = 0
for i in whiteSox2:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		whiteSox2[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		whiteSox2[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		whiteSox2[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		whiteSox2[counter - 1] = i / 10000

counter = 0
for i in royals2:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		royals2[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		royals2[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		royals2[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		royals2[counter - 1] = i / 10000

counter = 0
for i in diamondbacks2:
	diamondbacks2 += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		diamondbacks2[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		diamondbacks2[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		diamondbacks2[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		diamondbacks2[counter - 1] = i / 10000
counter = 0
for i in dodgers2:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		dodgers2[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		dodgers2[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		dodgers2[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		dodgers2[counter - 1] = i / 10000

counter = 0
for i in tigers2:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		tigers2[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		tigers2[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		tigers2[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		tigers2[counter - 1] = i / 10000
counter = 0
for i in rays2:
	counter += 1
	if (i ** 2) ** .5 > 1 and (i ** 2) ** .5 <= 10:
		rays2[counter - 1] = i / 10
	elif i > 10 and i <= 100:
		rays2[counter - 1] = i / 100
	elif i > 100 and i < 1000:
		rays2[counter - 1] = i / 1000
	elif i > 1000 and i < 10000:
		rays2[counter - 1] = i / 10000

weights = np.array([[1.41873609],
                    [-1.20625733],
                    [1.51404479],
                    [-1.87708384],
                    [-1.41562917],
                    [-1.352728],
                    [-1.94787091],
                    [1.37726651],
                    [1.14543346],
                    [1.4506023],
                    [1.25538474],
                    [-1.70979535],
                    [-1.16172174],
                    [-1.98569601],
                    [-1.54996447],
                    [1.09549003],
                    [-1.16129479],
                    [-1.36392377],
                    [-1.8911979],
                    [1.0572363],
                    [-2.25526817],
                    [1.50568136],
                    [-1.94992075],
                    [-1.38018242],
                    [-1.53204585],
                    [1.71746718],
                    [1.29098729],
                    [1.08493724],
                    [1.37974075],
                    [0.70749517],
                    [1.053839],
                    [0.94556788],
                    [-1.43507085],
                    [-1.80065257],
                    [-1.99531848],
                    [1.15438987],
                    [1.64096134],
                    [0.99108565],
                    [1.62149567],
                    [1.40972685],
                    [-1.14554508],
                    [-1.13649906],
                    [1.20027905],
                    [1.56848826],
                    [-0.90122385]])
bias = 5.6128284

LR = .00008


def back(x, y):
	weights = np.array([[1.41873609],
	                    [-1.20625733],
	                    [1.51404479],
	                    [-1.87708384],
	                    [-1.41562917],
	                    [-1.352728],
	                    [-1.94787091],
	                    [1.37726651],
	                    [1.14543346],
	                    [1.4506023],
	                    [1.25538474],
	                    [-1.70979535],
	                    [-1.16172174],
	                    [-1.98569601],
	                    [-1.54996447],
	                    [1.09549003],
	                    [-1.16129479],
	                    [-1.36392377],
	                    [-1.8911979],
	                    [1.0572363],
	                    [-2.25526817],
	                    [1.50568136],
	                    [-1.94992075],
	                    [-1.38018242],
	                    [-1.53204585],
	                    [1.71746718],
	                    [1.29098729],
	                    [1.08493724],
	                    [1.37974075],
	                    [0.70749517],
	                    [1.053839],
	                    [0.94556788],
	                    [-1.43507085],
	                    [-1.80065257],
	                    [-1.99531848],
	                    [1.15438987],
	                    [1.64096134],
	                    [0.99108565],
	                    [1.62149567],
	                    [1.40972685],
	                    [-1.14554508],
	                    [-1.13649906],
	                    [1.20027905],
	                    [1.56848826],
	                    [-0.90122385]])
	bias = 5.6128284
	
	LR = .00008
	actual = relu(np.dot(x, weights) + bias)
	
	weights -= np.reshape(.0005 * derivativeWeights(x, weights, actual, bias, y),
	                      (45, 1)) * LR
	bias -= .007 * derivativeBias(x, weights, actual, bias, y) * LR


for j in range(2000):
	actual = relu(np.dot(brewersRuns, weights) + bias)
	
	weights = weights - np.reshape(.0005 * derivativeWeights(brewersRuns, weights, actual, bias, 2),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(brewersRuns, weights, actual, bias, 2) * LR
	
	actual = relu(np.dot(marlinsRuns, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(marlinsRuns, weights, actual, bias, 1),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(marlinsRuns, weights, actual, bias, 1) * LR
	
	actual = relu(np.dot(redsRuns, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(redsRuns, weights, actual, bias, 8),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(redsRuns, weights, actual, bias, 8) * LR
	
	actual = relu(np.dot(piratesRuns, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(piratesRuns, weights, actual, bias, 2),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(piratesRuns, weights, actual, bias, 2) * LR
	
	actual = relu(np.dot(astrosRuns, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(astrosRuns, weights, actual, bias, 6),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(astrosRuns, weights, actual, bias, 6) * LR
	
	actual = relu(np.dot(nationalsRuns, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(nationalsRuns, weights, actual, bias, 1),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(nationalsRuns, weights, actual, bias, 1) * LR
	
	actual = relu(np.dot(marlinsRuns2, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(marlinsRuns2, weights, actual, bias, 3),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(marlinsRuns2, weights, actual, bias, 3) * LR
	
	actual = relu(np.dot(nationalsRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(nationalsRuns3, weights, actual, bias, 2),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(nationalsRuns3, weights, actual, bias, 2) * LR
	
	actual = relu(np.dot(marlinsRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(marlinsRuns3, weights, actual, bias, 8),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(marlinsRuns3, weights, actual, bias, 8) * LR
	
	actual = relu(np.dot(tigersRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(tigersRuns3, weights, actual, bias, 3),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(tigersRuns3, weights, actual, bias, 3) * LR
	
	actual = relu(np.dot(raysRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(raysRuns3, weights, actual, bias, 2),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(raysRuns3, weights, actual, bias, 2) * LR
	
	actual = relu(np.dot(yankeesRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(yankeesRuns3, weights, actual, bias, 6),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(yankeesRuns3, weights, actual, bias, 6) * LR
	
	actual = relu(np.dot(oriolesRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(oriolesRuns3, weights, actual, bias, 2),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(oriolesRuns3, weights, actual, bias, 2) * LR
	
	actual = relu(np.dot(marinersRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(marinersRuns3, weights, actual, bias, 2),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(marinersRuns3, weights, actual, bias, 2) * LR
	
	actual = relu(np.dot(blueJaysRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(blueJaysRuns3, weights, actual, bias, 6),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(blueJaysRuns3, weights, actual, bias, 6) * LR
	
	actual = relu(np.dot(astrosRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(astrosRuns3, weights, actual, bias, 3),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(astrosRuns3, weights, actual, bias, 3) * LR
	
	actual = relu(np.dot(redSoxRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(redSoxRuns3, weights, actual, bias, 6),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(redSoxRuns3, weights, actual, bias, 6) * LR
	
	"""actual = relu(np.dot(cardinalsRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(cardinalsRuns3, weights, actual, bias, 3),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(cardinalsRuns3, weights, actual, bias, 3) * LR

	actual = relu(np.dot(metsRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(metsRuns3, weights, actual, bias, ),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(metsRuns3, weights, actual, bias, 3) * LR"""
	
	actual = relu(np.dot(bravesRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(bravesRuns3, weights, actual, bias, 0),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(bravesRuns3, weights, actual, bias, 0) * LR
	
	actual = relu(np.dot(brewersRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(brewersRuns3, weights, actual, bias, 1),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(brewersRuns3, weights, actual, bias, 1) * LR
	
	actual = relu(np.dot(piratesRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(piratesRuns3, weights, actual, bias, 0),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(piratesRuns3, weights, actual, bias, 0) * LR
	
	actual = relu(np.dot(cubsRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(cubsRuns3, weights, actual, bias, 9),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(cubsRuns3, weights, actual, bias, 9) * LR
	
	actual = relu(np.dot(angelsRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(angelsRuns3, weights, actual, bias, 4),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(angelsRuns3, weights, actual, bias, 4) * LR
	
	actual = relu(np.dot(rangersRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(rangersRuns3, weights, actual, bias, 7),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(rangersRuns3, weights, actual, bias, 7) * LR
	
	actual = relu(np.dot(giantsRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(giantsRuns3, weights, actual, bias, 7),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(giantsRuns3, weights, actual, bias, 7) * LR
	
	actual = relu(np.dot(rockiesRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(rockiesRuns3, weights, actual, bias, 6),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(rockiesRuns3, weights, actual, bias, 6) * LR
	
	actual = relu(np.dot(twinsRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(twinsRuns3, weights, actual, bias, 3),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(twinsRuns3, weights, actual, bias, 3) * LR
	
	actual = relu(np.dot(athleticsRuns3, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(athleticsRuns3, weights, actual, bias, 1),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(athleticsRuns3, weights, actual, bias, 1) * LR
	
	actual = relu(np.dot(blueJays, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(blueJays, weights, actual, bias, 3),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(blueJays, weights, actual, bias, 3) * LR
	
	actual = relu(np.dot(mariners, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(mariners, weights, actual, bias, 0),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(mariners, weights, actual, bias, 0) * LR
	
	actual = relu(np.dot(yankees, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(yankees, weights, actual, bias, 5),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(yankees, weights, actual, bias, 5) * LR
	
	actual = relu(np.dot(orioles, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(orioles, weights, actual, bias, 4),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(orioles, weights, actual, bias, 4) * LR
	
	actual = relu(np.dot(padres, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(padres, weights, actual, bias, 3),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(padres, weights, actual, bias, 3) * LR
	
	actual = relu(np.dot(phillies, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(phillies, weights, actual, bias, 0),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(phillies, weights, actual, bias, 0) * LR
	
	actual = relu(np.dot(marlins, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(marlins, weights, actual, bias, 5),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(marlins, weights, actual, bias, 5) * LR
	
	actual = relu(np.dot(nationals, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(nationals, weights, actual, bias, 1),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(nationals, weights, actual, bias, 1) * LR
	
	actual = relu(np.dot(reds, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(reds, weights, actual, bias, 5),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(reds, weights, actual, bias, 5) * LR
	actual = relu(np.dot(guardians, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(guardians, weights, actual, bias, 4),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(guardians, weights, actual, bias, 4) * LR
	
	actual = relu(np.dot(twins2, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(twins2, weights, actual, bias, 14),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(twins2, weights, actual, bias, 14) * LR
	
	actual = relu(np.dot(athletics2, weights) + bias)
	weights = weights - np.reshape(.0005 * derivativeWeights(athletics2, weights, actual, bias, 4),
	                               (45, 1)) * LR
	bias -= .007 * derivativeBias(athletics2, weights, actual, bias, 4) * LR
	
	back(diamondbacks2, 3)
	back(dodgers2, 5)
	back(yankees2, 3)
	back(orioles2, 2)
	back(whiteSox2, 2)
	back(royals2, 4)
	back(tigers2, 1)
	back(rays2, 6)

print(relu(np.dot(yankees2, weights) + bias), relu(np.dot(orioles2, weights) + bias))

print(relu(np.dot(tigers2, weights) + bias), relu(np.dot(rays2, weights) + bias))

print(relu(np.dot(diamondbacks2, weights) + bias), relu(np.dot(dodgers2, weights) + bias))

print(relu(np.dot(whiteSox2, weights) + bias), relu(np.dot(royals2, weights) + bias))

print(relu(np.dot(twins2, weights) + bias), relu(np.dot(athletics2, weights) + bias))
print(weights, bias)
