"""from mpmath import *
import cmath
import matplotlib.pyplot as plt

temp = 1
for i in range(1,5000):
    if i % 100 == 0:
        plt.scatter(i,(cmath.log(i**2)))
    x = zeta(.5 + i*j)
    if ((x.imag)**2+(x.real)**2)**.5 > temp:
        temp = ((x.imag)**2+(x.real)**2)**.5
        plt.scatter(i,((x.imag)**2+(x.real)**2)**.5)
plt.show()"""
import numpy as np
import matplotlib.pyplot as plt
# The next library contains the zeta(), zetazero(), and siegelz() functions
from mpmath import *
import math
import random
mp.dps = 25;
mp.pretty = True


def graph_zeta(real, image_name):
    """A, B, C = [], [], []
    
    fig = plt.figure()
    ax = fig.add_subplot(111)"""
    run = 0
    for i in range(3,10):
        for j in range(2,i):
            print(math.factorial(i)+j)
        """ h = random.randint(5000000000,10000000000)
        function = abs(zeta(real + 1j * float(h)) / math.log(h))
        run += function
        function1 = siegelz(i)"""
        """plt.scatter(g*h, function1)"""
        """A.append(function)
        B.append(function1)
        C.append(h*g)"""
       
        """plt.scatter(i, 2.42*math.log(i+1)-6.9)"""

    """print(run / 100)"""
    """ax.grid(True)
    ax.plot(C, A, label='modulus of Riemann zeta function along critical line, s = 1/2 + it', lw=0.8)
    ax.set_title("Riemann Zeta function - re(s)=1/2")
    ax.set_ylabel("Z(t)")
    ax.set_xlabel("t")

    # Include legend
    leg = ax.legend(shadow=True)
    # Edit font size of legend to make it fit into chart
    for t in leg.get_texts():
        t.set_fontsize('small')
    # Edit the line width in the legend
    for l in leg.get_lines():
        l.set_linewidth(2.0)
    # Plot the zeroes of zeta
    for i in range(5):
        zero = zetazero(start + i)
        ax.plot(zero.imag, [0.0], "ro")

    # save plot and print that it was saved
    ax.set_ylim(-15,15)
    plt.show()
    plt.close()"""


graph_zeta(0.5, "Z(t)_Plot.png")