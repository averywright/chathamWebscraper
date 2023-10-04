import random
g = 0
for i in range(1000000):
	x = random.randint(1, 6)
	y = random.randint(1, 6)
	z = random.randint(1, 6)

	
	if (x > y or x == y) and (y > z or y ==z):
		g += x+y
	elif (x > z or x == z) and (z > y or z == y):
		g += (x+z)
	elif (y > x or x == y) and (x > z or x ==z):
		g += (x+y)
	
	elif (y > z or z == y) and (z > x or x ==z):
		g += (z+y)
	
	elif (z > y or z == y) and (y > x or y ==x):
		g += (z+y)
	
	elif (z > x or x == z) and (x > y or y ==x):
		g += (x+z)

print(g / 1000000)




