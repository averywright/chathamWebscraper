import numpy as np
import random
import cmath

brain_mold = np.zeros(1000, dtype=complex)
counter = 0
for i in brain_mold:
    counter += 1
    brain_mold[counter-1] = complex(random.randrange(-10, 10), random.randrange(-10, 10))


def base_six(z):
    inputs = []
    for i in z:
        counter = 0
        accounted = True
        for j in 'abcdefghijklmnopqrstuvwxyz':
            counter += 1
            if i == j:
                inputs.append(counter)
                accounted = False
        if accounted:
            inputs.append(0)
    counter = 0
    for i in inputs:
        counter += 1
        inputs[counter - 1] = (int(i/6)*10) + (i % 6)
    return inputs


running = True
while running:
    user_message = input('What would you like to say? ')
    numbered_input = base_six(user_message)
    message_length = len(base_six(user_message))
    desired_message = base_six(input('What response do you want? '))
    first_weights = np.random.randn(4, message_length)
    second_weights = np.random.randn(4, message_length)
    outcome_try = []
    desired_len = random.randint()
    while np.all(outcome_try) != np.all(desired_message):


