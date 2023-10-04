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


all = []

tps = []
total = [7]
checker = []
poss = [900]

for k in poss:
    gg = 0
    print(k)
    for i in range(1000, 11000):
        holding = []
        mult = ((i**2) * k) - 1
        print(mult)
        print("n = " + str(i))
        for j in range(2, int(mult**.5)+3):
            primed = []
            if mult % j == 0:
                if j < (mult** .5) - 3:
                    break
                if isprime(j):
                    print("| " + str(j))
                    holding.append(j)
                    if isprime(j) and isprime(j+2):
                        for l in total:
                            if l == j:
                                primed = False
                        if primed:
                            total.append(j)
                    elif isprime(j) and isprime(j-2):
                        for l in total:
                            if l == j:
                                primed = False
                        if primed:
                            total.append(j)
        if len(holding) == 2 and holding[1] - holding[0] == 2:
            tps.append(i)
            gg += 1
        if len(holding) == 2 and holding[1] - holding[0] != 2:
            all.append(i)

        checker = holding.copy()
    print(" | " + str(gg))

