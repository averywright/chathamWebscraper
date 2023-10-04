import nhl
a = .54
b = .54
c = -11


def root(x):
	print(x)
	if (a*(x**2)+b*x+c) < .001 and (a*(x**2)+b*x+c) > -.001:
		return x
	else:
		root(x-(a*(x**2)+b*x+c)/(2*a*x+b))
	
print(root(.54))