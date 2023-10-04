import random


a = [0,1,2,3,4,5,6,7]
g= 0
for i in range(10000):
	b = []
	for i in range(3):
		x =  random.randint(0, 7)
		b.append(x)
	
	value = False
	print(b)
	for i in b:
		if i == 5:
			value = True
		elif i == 6 or i==7:
			value = False
			break
	if value:
		g+=1
		
print(g/10000)

