import numpy as np

training = [[1, 0, 1, 0],[1, 1, 1, 1], [0,1,1,1], [0,0,1,0]]

solutions = [1, 1, 0, 0]

weights = np.random.randn(4)

attempt = []


while attempt != solutions:
    attempt = [np.dot(training[0], weights),
    np.dot(training[1], weights),
    np.dot(training[2], weights),
    np.dot(training[3], weights)]


"""
weights * inputs + biases = x
RELU or Sigmoid function (RELU(x))


"""

