import random
possibles = [7, 11, 13,17,19,29,31,41,43,101,103,59,61,227,229, 659, 661, 347, 349, 241, 239, 199, 197, 71, 73, 1078409, 1078411, 137 , 139, 16831, 16829, 107, 109, 131863939, 131863937, 2081, 2083, 881, 883, 1871, 1873, 199, 197, 32369, 32371, 1021, 1023, 1114721, 1114723, 2945147, 2945149, 16189, 16187, 827, 829, 278741, 278743, 5881, 5879, 89671, 89669, 2339, 2341, 30559, 30557]

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


counter = 0
c = 0
for i in possibles:
    counter += 1
    mult = 3 * i
    if isprime(mult - 2) or isprime(mult + 2):
        c += 1
        print("T")
    else:
        print("F")

print(c/counter)