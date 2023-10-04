import math
"""import matplotlib.pylab as plt"""
def check(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to float(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True# A function to prfloat all prime factors of
# a given number n

g=0
for i in range(3,90000):
	if g > 0 and i > g+2:
		if check(i):
			print(((2*math.log(g)/math.log(g-2))))
			g = 0
	if check(i) and check(i+2):
		g = i+2

