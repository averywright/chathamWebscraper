import math


def check(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True# A function to print all prime factors of
# a given number n

def tp(x):
	if check(x):
		if check(x+2):
			return True
		if check(x-2):
			return True


def pf(n):
	listed = []
	
	# Print the number of two's that divide n
	while n % 2 == 0:
		listed.append(2)
		n = n / 2
	
	# n must be odd at this point
	# so a skip of 2 ( i = i + 2) can be used
	try:
		for i in range(3, int(math.sqrt(n)) + 1, 2):
			
			# while i divides n , print i and divide n
			while n % i == 0:
				listed.append(i)
				n = n / i
		
		# Condition if n is a prime
		# number greater than 2
		if n > 2:
			listed.append(n)
		return listed
	except:
		return [n]

def abs(x):
	return (x**2)**.5


def primer(n):
	hah = []
	prime = [True for i in range(n + 1)]
	p = 2
	while (p * p <= n):
		
		# If prime[p] is not
		# changed, then it is a prime
		if (prime[p] == True):
			
			# Update all multiples of p
			for i in range(p * p, n + 1, p):
				prime[i] = False
		p += 1
	for p in range(4, n + 1):
		if check(p) and check(p+2):
			hah.append(p)
			hah.append(p+2)
	return hah



"""
counter = 0
for i in primes:
	counter +=1
	if counter % 2 == 0:
		print(primes[counter-2] * primes[counter-1] )
		print(pf((primes[counter-2] * primes[counter-1])-1))
		print(pf((primes[counter - 2] * primes[counter - 1]) + 1))"""
output = []
for j in range(11, 10000):
	if primer(j) != primer(j-1):
		primes = primer(j)

		if len(primes) % 4 == 0:
			prod = 1
			for i in primes:
				prod *= i
			print(primes)
			print(prod)
			res = 1


			for i in pf(prod+1):
				res *= i

			final = []
			final = pf(prod+1)
			for i in pf(prod-1):
				final.append(i)

			unfinished = True
			while unfinished:
				unfinished = False
				for i in final:
					if not tp(i) and i != 2:
						unfinished = True
						final.remove(i)
						for j in pf(i - 1):
							final.append(j)
						for j in pf(i + 1):
							final.append(j)

			print(final)





			"""x = pf(prod+1)[len(pf(prod+1))-1]
			while not (((check(x)) and check(x-2)) or ((check(x)) and check(x+2))):
				prod = pf(prod+1)[len(pf(prod+1))-1]
				x = pf(prod+1)[len(pf(prod+1))-1]
			output.append(x)
			res = 1
			
			for i in pf(prod-1):
				res *= i
			x = pf(prod-1)[len(pf(prod-1))-1]
			while not (((check(x)) and check(x-2)) or ((check(x)) and check(x+2))):
				prod = pf(prod-1)[len(pf(prod-1))-1]
				x = pf(prod-1)[len(pf(prod-1))-1]
			output.append(x)
			
			print(output)"""
			


"""for i in pf(prod+1):
	res *= i
for i in pf(prod-1):
	res *= i
print(res)"""

"""for i in range(2,900000):
	if primer(i) == True:
		primes.append(i)
		
""""""
x = 0
y = 0
counter = 0
listed = [[0,0]]
for i in primes:
	if counter % 4 == 0:
		x += i
		plt.scatter(abs(x), abs(y), color ='red')
	elif counter % 4 == 1:
		y -= i
		plt.scatter(abs(x), abs(y), color = 'blue')
	elif counter % 4 == 2:
		x -= i
		plt.scatter(abs(x), abs(y), color= 'black')
	elif counter % 4 == 3:
		y += i
		plt.scatter(abs(x), abs(y),color = 'green')
	counter += 1
	listed.append([abs(x),abs(y)])

running = 0
counter =  0
for i in listed:
	counter += 1
	running += 1/(((counter-i[0])**2 + (counter-i[1])**2)**1.76)

print(running)

counter = 0
for i in primes:
	try:
		if i - primes[counter+1] == -2:
			print(i)
	except:
		error = True
	counter += 1

counter = 0
for i in listed:
	print(i)
	try:
		print(primes[counter])
	except:
		error = True
	counter += 1

g = 0
counter = 1
for i in range(1, len(listed)):
	if counter % 4 == 0:
		rect = (listed[counter+1][1] - listed[counter+2][1])*(listed[counter+1][0] - listed[counter+3][0])
		tri = (listed[counter][0] - listed[counter+4][0])*(listed[counter+4][1] - listed[counter][1])/2
		print(1/(rect+tri))
		g += 1 / (rect + tri)
	counter += 1
	if (listed[counter][1]**2 + listed[counter][0]**2)**.5 % 1 == 0:
		print(((listed[counter][1])**2 + (listed[counter][0])**2)**.5, listed[counter])
	g += 1 / ((listed[counter][1])**2 + (listed[counter][0])**2)**.5
	counter += 1
	
print(g)
plt.show()


1/2 + 1/ +
"""