import numpy as np
import random
import math

weights = np.array([[  2.63798937e-03],
       [  9.35010932e-05],
       [  9.01193718e-03],
       [ -5.45829387e-01],
       [ -3.68632404e+00],
       [  2.25363326e-02],
       [  1.07288842e-01],
       [ -2.96681326e-01],
       [  1.92913482e-02],
       [ -4.04575694e-01],
       [  1.93270641e-02],
       [  1.04043725e+00],
       [ -1.41286724e+00],
       [  3.53470153e-02],
       [  3.98188754e-01],
       [ -3.21072637e-01],
       [  3.60387824e-02],
       [  1.93281691e-02],
       [ -6.34791491e-03],
       [  1.60068584e-05],
       [  7.09576316e-03],
       [  6.42574664e-03],
       [  3.86194627e-02]])

bias = 1.51225684e-05
"""
kings27 = np.array([6.6,	0.92,	98.6,	3783,	3169,	54.4,	176.6,	161.9,	149,	148,	-14,	1903,	1698,	52.8,	580,	516,	52.9,	74,	11.3,	67,	11.5, 0, 3])
kraken27 = np.array([7.5,	0.908,	98.4	,3348,	3297,	50.4	,152.9	,155.1	,145,	180,	-33,	1532,	1598,	48.9,	454,	499,	47.6,	43,	8.7,	76,	13.2, 1, -1])

goldenknights27 =  np.array([7.6,
0.92,
99.6,
3894,
3543,
52.4,
196.1,
172.1,
175,
161,
- 10,
1920,
1757,
52.2,
642,
561,
53.4,
82,
11.3,
81,
12.6, 0 , -3])
Blackhawks	= np.array([7.3,	0.917,	98.9,	3229,	3777,	46.1,	151.5,	175.1,	138,	187,	-25,	1513,	1811,	45.5,	399,	492,	44.8,	49,	10.9,	79,	13.8, 1, -1])

Coyotes = np.array([8.5,	0.911,	99.6,	3037,	3877,	43.9,	144.5,	204.4,	150,	215,	-5,	1502,	1916,	43.9,	467,	614,	43.2,	64,	12.1,	93,	13.2, 0, -3])
Stars = np.array([7.1,	0.926,	99.7,	3458,	3625,	48.8,	172.9,	170.9,	143,	155,	-14,	1788,	1691,	51.4,	563,	505,	52.7,	65,	10.4,	64,	11.2, 1, -1])

Canadiens =	np.array([7.2,	0.914,	98.6,	3259,	3669,	47,	159.4,	193.1,	141,	193,	-18,	1619,	1935,	45.6,	525,	626,	45.6,	62,	10.6,	94,	13.1, 0, -5])
Rangers = np.array([8,	0.931,	101.1,	3202,	3596,	47.1,	158.6,	172.2,	154,	143,	25,	1579,	1812,	46.6,	482,	558,	46.3,	74,	13.3,	62,	10, 1, 1])

Flyers = np.array([7.8,	0.918,	99.7,	3313,	3822,	46.4,	158.9,	181.4,	159,	186,	-5,	1598,	1838,	46.5,	527,	574,	47.9,	74,	12.3,	74,	11.4, 0, -1])
Jets =	np.array([7.3,	0.925,	99.8,	3439,	3523,	49.4,	179,	181,	149,	159,	-8,	1782,	1812,	49.6,	554,	576,	49,	70,	11.2,	60,	9.4, 1,-3 ])
"""
"""Bruins29 = np.array([6.8,.924,99.2,3781,3145,54.6,194.6,140.9,171,141,-24,1810,1456,55.4,578,443,56.6,79,12.0,68,13.3, 0, 3])
Leafs29 = np.array([8.6,.915,100.1,3942,3435,53.4,206.2,165.6,205,181,-17,2130,1757,54.8,611,479,56.1,77,11.2,74,13.4, 1, -1])

Flames29 = np.array([8.1,.929,100.9,4064,3202,55.9,195.3,151.4,195,137,14,2015,1572,56.2,570,458,55.4,65,10.2,53,10.4, 0, 1])
Jets29 = np.array([7.2,.926,99.9,3473,3568,49.3,180.5,182.5,150,159,-7,1803,1832,49.6,562,581,49.2,71,11.2,60,9.4, 1, -1])

Blackhawks29 = np.array([7.3,.917,99.0,3282,3842,46.1,153.6,177.5,141,190,-25,1534,1839,45.5,406,494,45.1,50,11.0,79,13.8, 0, 1])
Sabres29 = np.array([7.6,.914,99.0,3327,3556,48.3,155.6,183.4,156,198,-14,1541,1755,46.8,448,545,45.1,66,12.8,79,12.7, 1, 3])

Lightning29 = np.array([8.8,.925,101.4,3405,3275,51.0,175.9,161.9,179,146,19,1814,1675,52.0,536,491,52.2,75,12.3,69,12.3, 0, 3])
Islanders29 = np.array([7.9,.931,101.0,3289,3875,45.9,171.4,195.4,156,156,24,1710,1935,46.9,512,588,46.5,73,12.5,64,9.8, 1, -1])

Avalanche29 = np.array([8.6,.928,101.3,3805,3388,52.9,182.4,171.5,197,150,36,1832,1688,52.0,531,569,48.3,72,11.9,73,11.4, 0, -3])
Wild29 = np.array([9.3,.925,101.8,3541,3348,51.4,181.8,149.8,204,149,23,1767,1482,54.4,506,417,54.8,79,13.5,60,12.6, 1, 3])

Predators29 = np.array([8.1,.927,100.8,3376,3456,49.4,156.8,166.3,161,151,20,1678,1702,49.6,475,460,50.8,75,13.6,67,12.7, 0, -1])
Coyotes29 = np.array([8.5,.911,99.6,3079,3922,44.0,148.0,205.8,152,217,-7,1528,1941,44.0,476,620,43.4,64,11.9,94,13.2, 1, -1])"""

"""capitals5 = np.array([8.3,.922,100.5,3635,3552,50.6,175.2,166.5,179,157,13,1811,1756,50.8,531,545,49.3,70,11.6,70,11.4, 0,1 ])
predators5 = np.array([8.5,.919,100.4,4142,3178,56.6,223.2,164.5,218,161,-2,2186,1644,57.1,680,577,54.1,87,11.3,64,10.0,1, -1 ])
"""
capitals = np.array([8.3,.922,100.5,3635,3552,50.6,175.2,166.5,179,157,13,1811,1756,50.8,531,545,49.3,70,11.6,70,11.4, 0, 0])
panthers= np.array([8.5,.919,100.4,4142,3178,56.6,223.2,164.5,218,161,-2,2186,1644,57.1,680,577,54.1,87,11.3,64,10.0, 1, 0])

def sigmoid(x):
    sig = 1 / (1 + np.exp(-x))
    return sig


"""actual = np.dot((Bruins29-Leafs29), weights) + bias
print("Bruins v Leafs", sigmoid(actual))

actual = np.dot((Flames29-Jets29), weights) + bias
print("Flames v Jets", sigmoid(actual))

actual = np.dot((Blackhawks29 - Sabres29), weights) + bias
print("Blackhawks v Sabres", sigmoid(actual))

actual = np.dot((Lightning29-Islanders29), weights) + bias
print("Lightning v Islanders", sigmoid(actual))

actual = np.dot((Avalanche29-Wild29), weights) + bias
print("Avalanche29 v Wild29", sigmoid(actual))

actual = np.dot((Predators29-Coyotes29), weights) + bias
print("Predators29 v Coyotes29", sigmoid(actual))
"""

actual = np.dot((capitals-panthers), weights) + bias
print(sigmoid(actual))