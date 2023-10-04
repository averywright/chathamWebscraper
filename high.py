import numpy as np
import random

def reLU(z):
    try:
        for i in z:
            if i < 0:
                i =0
    except:
        print('e')

    try:
        for i in z:
            for j in i:
                if j < 0:
                    j = 0
    except:
        print('e')

    return z


def matri(z):
    speech = 'abcdefghijklmnopqrstuvwxyz ,.'
    matrixform = []
    for i in z:
        counter = 0
        for j in speech:
            counter += 1
            if i == j:
                matrixform.append(counter - 1)

    return matrixform


def layer(inputs, w, b):
    wPlaceHold = w.copy()
    count = 0
    for i in wPlaceHold:
        count += 1
        i = i.reshape(len(i), 1)
        i = np.dot(inputs, i) + b[count - 1]

    return np.array(reLU(wPlaceHold))


w1 = np.random.randn(29, 29)
w2 = np.random.randn(841, 29)
w3 = np.random.randn(29, 841)

b1 = np.random.randn(29)
b2 = np.random.randn(841)
b3 = np.random.randn(29)

for i in range(1):
    message = raw_input('Enter your message: ')
    responseIdeal = raw_input('How should I respond? ')
    inputs = np.array(matri(message))
    idealz = np.array(matri(responseIdeal))
    stageOne = layer(inputs, w1, b1)
    stageTwo = layer(stageOne, w2, b2)
    stageThree = layer(stageTwo, w3, b2)

    print(stageThree)







