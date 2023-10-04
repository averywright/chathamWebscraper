"""import matplotlib.pyplot as plt"""
import math
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

def factors(n):
	factors = [1,n]
	i = 2
	# This will loop from 2 to float(sqrt(x))
	while i * i <= n:
		# Check if i divides x without leaving a remainder
		if n % i == 0:
			# This means that n has a factor in between 2 and sqrt(n)
			# So it is not a prime number
			factors.append(i)
		i += 1
	# If we did not find any factor in the above loop,
	# then n is a prime number
	return factors

primes = []
running = 0
end = 50
num = 0
for i in range(7, end):
	if check(i):
		primes.append(i)

running = 0
count = 0
stringy = ''
"""for j in range(2, int(primes[2] / 2) + 1):
	stringy += str(primes[2] % j)
print(stringy)
"""
for i in primes:
	stringy = ''
	count += 1
	for j in range(3, int(i/2)+1):
		stringy += str(i%j)
	print(factors(float(stringy)))
	"""print(str(i) + ': ' + str(float(stringy)%(int(i/2)+1)))"""
	"""plt.scatter(i,(float(stringy)%i))"""
"""plt.show()"""
"""
a 00000
b 00001
c 00010
d 00011
e 00100
f 00101
g 00110
h 00111
i 01000
j 01001
k 01010
l 01011
m 01100
n 01101
o 01110
p 01111
q 10000
r 10001
s 10010
t 10011
u 10100
v 10101
w 10110
x 10111
y 11000
z 11001
11010
11011
11100
11110
11111
"""