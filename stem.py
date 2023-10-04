import math

# A function to print all prime factors of
# a given number n
def pf(n):
	listed = []
    
    # Print the number of two's that divide n
	while n % 2 == 0:
		listed.append(2)
		n = n / 2
        
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
	try:
		for i in range(3,int(math.sqrt(n))+1,2):
	        
	        # while i divides n , print i and divide n
			while n % i== 0:
				listed.append(i)
				n = n / i
	    
	    # Condition if n is a prime
	    # number greater than 2
		if n > 2:
			listed.append(n)
		return listed
	except:
		return [n]
# Driver Program to test above function

"""from math import comb


def AKS(n):
	if (n % 2== 0):  # check if it's even
		if n == 2:
			return True
		return False
	for i in range(3, n // 2):
		if comb(n, i) % n != 0:  # check if any coefficient isn't divisible by n
			return False
	return True


def new(input):
	n = 1
	for i in input:
		n *= i
	starters = []
	for i in pf(n+1):
		starters.append(i)
	for i in pf(n-1):
		starters.append(i)

	
	for i in starters:
		use = True
		for j in input:
			if j == i:
				use = False
		if use:
			if i != 2 and i != 3:
				try:
					if (pf(int(i)) and pf(int(i+2))) or (pf(int(i)) and pf(int(i-2))):
						input.append(i)
				except:
					print('e')
	counter = 0
	for i in starters:
		counter += 1
		if counter == 1:
			break
		for j in pf(i+1):
			starters.append(j)
	return input

primes = []
g = [5,7,13]
for k in range(10):
	for i in g:
		add = True
		for j in primes:
			if j == i:
				add = False
		if add:
			primes.append(i)
	g = new(g)
	g.remove(g[0])
	g.remove(g[0])
	print(primes)
	
print(primes)
c = float(1)
for i in primes:
	c += float(i)
print(float(c))
"""

print(pf(50))