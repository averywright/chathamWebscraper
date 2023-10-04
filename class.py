import numpy as np
import matplotlib.pylab as plt

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

c = 0
yaxis = []
"""for i in range(5, 10000):"""
g = (6*678) - 1
if not isprime(g):
    while not (isprime(g) and isprime(g-2) ) or (isprime(g) and isprime(g+2)):
        if isprime(g):
            for j in range(2, (g+2)**.5):
                if (g+2) % j == 0:
                    if isprime(j):
                        c = j

        g = c



print(g)


