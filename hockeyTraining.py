import numpy as np
import random
import math

"""bluejackets26 = np.array([8.5,.915,100.0,3419,3752,47.7,155.9,205.2,173,206,16,1610,1856,46.5,464,532,46.6,71,13.3,68,11.3, 0, -3])
lightning26 = np.array([8.9,.925,101.4,3334,3178,51.2,172.6,159.0,176,143,19,1772,1636,52.0,526,482,52.2,74,12.3,68,12.4, 1, 3])

panthers26 = np.array([8.5,.921,100.6,3997,3035,56.8,215.6,155.8,212,149,3,2109,1567,57.4,655,548,54.4,84,11.4,56,9.3, 0, 3])
bruins26 = np.array([6.8,.922,99.0,3708,3068,54.7,189.6,137.0,165,140,-28,1768,1419,55.5,562,431,56.6,75,11.8,68,13.6, 1, 3])

oilers26 = np.array([7.8,.920,99.9,3743,3351,52.8,184.8,175.1,174,167,-3,1755,1752,50.0,509,495,50.7,85,14.3,66,11.8,0, 3])
penguins26 =np.array( [7.5,.929,100.4,3744,3447,52.1,192.8,170.3,174,150,2,1845,1604,53.5,528,502,51.3,78,12.9,68,11.9,1, 1])

devils26 = np.array([7.9,.906,98.5,3649,3587,50.4,176.9,169.3,171,205,-42,1814,1710,51.5,521,466,52.8,79,13.2,89,16.0, 0, -3])
senators26 = np.array([7.3,.923,99.5,3427,3733,47.9,157.8,182.5,145,171,-1,1666,1843,47.5,534,543,49.6,54,9.2,77,12.4, 1,1])

islanders26 = np.array([7.9,.930,100.9,3220,3782,46.0,168.8,191.6,153,154,22,1673,1899,46.8,504,575,46.7,73,12.7,64,10.0, 0, -5])
capitals26 =np.array( [8.5,.922,100.7,3492,3443,50.4,169.2,161.7,176,151,18,1754,1703,50.7,511,533,48.9,69,11.9,69,11.5, 1, 1])

hurricanes26 = np.array([8.0,.927,100.7,3940,3045,56.4,180.8,155.9,184,136,23,1864,1580,54.1,637,507,55.7,86,11.9,63,11.1, 0, 3])
rangers26 = np.array([8.0,.931,101.2,3169,3552,47.2,156.5,169.7,152,140,25,1560,1785,46.6,477,547,46.6,73,13.3,60,9.9, 1, 3])

redwings26 =np.array( [7.9,.914,99.3,3152,3718,45.9,167.9,204.6,155,200,-8,1558,1962,44.3,471,579,44.9,64,12.0,77,11.7,0, -1])
mapleleafs26 = np.array([8.6,.914,100.1,3889,3407,53.3,204.3,164.2,203,181,-18,2103,1746,54.6,601,477,55.8,77,11.4,74,13.4, 1, 1])

coyotes26 = np.array([8.4,.911,99.6,2998,3834,43.9,142.9,201.9,147,212,-6,1482,1891,43.9,459,605,43.1,63,12.1,91,13.1, 0, -5])
wild26 = np.array([9.3,.926,101.9,3459,3263,51.5,177.1,146.4,200,144,25,1723,1448,54.3,492,406,54.8,77,13.5,59,12.7,1,5 ])

flames26 =np.array( [8.1,.929,101.0,3977,3132,55.9,191.7,148.7,192,134,15,1986,1539,56.3,565,450,55.7,64,10.2,52,10.4, 0, 3])
predators26 =np.array( [8.1,.927,100.7,3298,3359,49.5,153.0,161.4,156,147,17,1641,1654,49.8,461,451,50.5,74,13.8,64,12.4, 1, -1])

goldenknights26 = np.array([7.6,.920,99.6,3837,3487,52.4,194.6,169.6,174,159,-10,1893,1734,52.2,635,553,53.5,82,11.4,80,12.6, 0, -1])
stars26 = np.array([7.1,.925,99.6,3402,3568,48.8,170.5,168.9,141,154,-15,1765,1664,51.5,555,498,52.7,64,10.3,64,11.4, 1, -3])

blues26 = np.array([9.7,.925,102.1,3192,3529,47.5,182.0,179.6,196,161,33,1788,1939,48.0,489,565,46.4,64,11.6,65,10.3, 0, 3])
avs26 =np.array( [8.5,.928,101.3,3684,3302,52.7,177.0,166.6,190,146,34,1775,1646,51.9,518,551,48.5,68,11.6,72,11.6,1, -3])

kraken26 = np.array([7.6,.909,98.5,3308,3262,50.4,151.3,152.7,144,176,-31,1513,1579,48.9,449,496,47.5,43,8.7,75,13.1, 0, 1])
canucks26 = np.array([7.3,.933,100.6,3474,3535,49.6,165.3,171.5,149,138,17,1724,1744,49.7,495,505,49.5,58,10.5,61,10.8, 1, -1])

ducks26 = np.array([7.5,.917,99.2,3382,3704,47.7,166.9,181.2,149,183,-20,1625,1777,47.8,507,524,49.2,72,12.4,59,10.1, 0, -3])
sharks26 = np.array([7.3,.921,99.4,3249,3931,45.3,154.5,175.3,138,171,-12,1575,1787,46.8,522,539,49.2,62,10.6,69,11.3, 1, 1])

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

weights = np.random.rand(23,1) / 10000
bias = random.random() / 10000"""


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
    da = deriv(np.dot(x, y)+g)
    db = dc * da
    return db


def derivativeWeights(x, y, z, g, h):
    dc = z - h
    da = deriv(np.dot(x, y)+g)
    dz = x
    dw = dz * dc * da
    return dw


"""while (sigmoid(np.dot(a-b, weights) + bias)) != 1:
    actual = (sigmoid(np.dot(a-b, weights) + bias))
    weights = weights - np.reshape(.05 * derivativeWeights(a-b, weights, actual, bias), (13, 1))
    bias -= .05 * derivativeBias(a-b, weights, actual, bias)
    print(weights, bias, actual)"""

for i in range(10000):
    for i in range(1):
        actual = (sigmoid(np.dot(bluejackets26 - lightning26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(bluejackets26 - lightning26, weights, actual, bias, 0), (23, 1))
        bias -= .05 * derivativeBias(bluejackets26 - lightning26, weights, actual, bias, 0)
    for i in range(1):
        actual = (sigmoid(np.dot(panthers26 - bruins26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(panthers26 - bruins26, weights, actual, bias, 0),
                                       (23, 1))
        bias -= .05 * derivativeBias(panthers26 - bruins26, weights, actual, bias, 0)
    for i in range(1):
        actual = (sigmoid(np.dot(oilers26 - penguins26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(oilers26 - penguins26, weights, actual, bias,1 ),
                                       (23, 1))
        bias -= .05 * derivativeBias(oilers26 - penguins26, weights, actual, bias, 1)
    for i in range(1):
        actual = (sigmoid(np.dot(devils26 - senators26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(devils26 - senators26, weights, actual, bias, 0),
                                       (23, 1))
        bias -= .05 * derivativeBias(devils26 - senators26, weights, actual, bias,0 )
    for i in range(1):
        actual = (sigmoid(np.dot(islanders26 - capitals26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(islanders26 - capitals26, weights, actual, bias, 1),
                                       (23, 1))
        bias -= .05 * derivativeBias(islanders26 - capitals26, weights, actual, bias, 1)
    for i in range(1):
        actual = (sigmoid(np.dot(hurricanes26 - rangers26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(hurricanes26 - rangers26, weights, actual, bias, 1),
                                       (23, 1))
        bias -= .05 * derivativeBias(hurricanes26 - rangers26, weights, actual, bias,1 )
    for i in range(1):
        actual = (sigmoid(np.dot(redwings26 - mapleleafs26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(redwings26 - mapleleafs26, weights, actual, bias, 0),
                                       (23, 1))
        bias -= .05 * derivativeBias(redwings26 - mapleleafs26, weights, actual, bias, 0)
    for i in range(1):
        actual = (sigmoid(np.dot(coyotes26 - wild26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(coyotes26 - wild26, weights, actual, bias,1 ),
                                       (23, 1))
        bias -= .05 * derivativeBias(coyotes26 - wild26, weights, actual, bias,1 )
    for i in range(1):
        actual = (sigmoid(np.dot(flames26 - predators26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(flames26 - predators26, weights, actual, bias,1 ),
                                       (23, 1))
        bias -= .05 * derivativeBias(flames26 - predators26, weights, actual, bias, 1)
    for i in range(1):
        actual = (sigmoid(np.dot(goldenknights26 - stars26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(goldenknights26 - stars26, weights, actual, bias, 0),
                                       (23, 1))
        bias -= .05 * derivativeBias(goldenknights26 - stars26, weights, actual, bias,0 )
    for i in range(1):
        actual = (sigmoid(np.dot(blues26 - avs26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(blues26 - avs26, weights, actual, bias,0 ),
                                       (23, 1))
        bias -= .05 * derivativeBias(blues26 - avs26, weights, actual, bias, 0)
    for i in range(1):
        actual = (sigmoid(np.dot(kraken26 - canucks26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(kraken26 - canucks26, weights, actual, bias, 0),
                                       (23, 1))
        bias -= .05 * derivativeBias(kraken26 - canucks26, weights, actual, bias,0 )
    for i in range(1):
        actual = (sigmoid(np.dot(ducks26 - sharks26, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(ducks26 - sharks26, weights, actual, bias,1 ),
                                       (23, 1))
        bias -= .05 * derivativeBias(ducks26 - sharks26, weights, actual, bias, 1)
        
    for i in range(1):
        actual = (sigmoid(np.dot(Flyers - Jets, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(Flyers - Jets, weights, actual, bias,0 ),
                                       (23, 1))
        bias -= .05 * derivativeBias(Flyers - Jets, weights, actual, bias, 0)
    for i in range(1):
        actual = (sigmoid(np.dot(Canadiens - Rangers, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(Canadiens - Rangers, weights, actual, bias,1 ),
                                       (23, 1))
        bias -= .05 * derivativeBias(Canadiens - Rangers, weights, actual, bias, 1)
    for i in range(1):
        actual = (sigmoid(np.dot(Coyotes - Stars, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(Coyotes - Stars, weights, actual, bias,1 ),
                                       (23, 1))
        bias -= .05 * derivativeBias(Coyotes - Stars, weights, actual, bias, 1)
    for i in range(1):
        actual = (sigmoid(np.dot(goldenknights27 - Blackhawks, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(goldenknights27 - Blackhawks, weights, actual, bias, 0),
                                       (23, 1))
        bias -= .05 * derivativeBias(goldenknights27 - Blackhawks, weights, actual, bias, 0)
    for i in range(1):
        actual = (sigmoid(np.dot(kings27 - kraken27, weights) + bias))
        weights = weights - np.reshape(.05 * derivativeWeights(kings27 - kraken27, weights, actual, bias,1 ),
                                       (23, 1))
        bias -= .05 * derivativeBias(kings27 - kraken27, weights, actual, bias, 1)

print(weights, bias)
    