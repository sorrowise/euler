# time cost = 276 ms ± 1.39 ms

from itertools import count
from sympy import isprime

def main():
    k = 0
    for i in count(3,2):
        a = i**2 - (i-1)
        b = a - (i-1)
        c = b - (i-1)
        k += len([x for x in [a,b,c] if isprime(x)])
        n = 2 * i - 1
        if k/n < 0.1:
            return i
