import numpy as np
import matplotlib.pylab as plt


def isprime(n):
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



"""
There exists some finite set of twin primes, S, such that every natural integer 
can be 'twin prime factored' into twin primes contained in the set S.

30 : {29}, {31}
60 : {59}, {61}
90 : {7, 13}
120 : {7, 17}, {11, 11}
150 : {149}, {151}
180 : {179}, {181}
210 : {11, 19}
240 : {239}, {241}
270 : {269}, {271}
300 : {13, 7, 3}, {7, 43}
330 : {7, 7, 7}, {7, 7, 5}
360 : {19, 19}
390 : {17, 7, 3}, {17, 5, 5}
420 : {419}, {421}
450 : {11, 41}
480 : {13, 7, 5}, {13, 3, 13}
510 : {7, 73}
540 : {7, 7, 11}
570 : {569}, {571}
600 : {599}, {601}
630 : {17, 7, 5}, {17, 3, 13}
660 : {659}, {661}
690 : {13, 3, 17}, {13, 11, 5}
720 : {7, 103}
750 : {7, 107}
780 : {19, 41}, {11, 71}
810 : {809}, {811}

for any value 6n, if if n-1 is prime,
go to n+1, and vice versa. If both are prime, then stop,
twin primes are already found. Else, take the prime factorization.
Until every prime factor is a twin prime, keep going. In order to keep going, 
add or subtract two and try again with that integer, branching off and forming a
larger and larger tree.


"""