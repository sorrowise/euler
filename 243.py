# time cost = 49.4 ms ± 395 µs

from sympy import prime
from fractions import Fraction as f
from math import prod

def main(a=15499,b=94744):
    fy = lambda n:prod([prime(i) for i in range(1,n+1)])
    fx = lambda n:prod([prime(i)-1 for i in range(1,n+1)])
    n = 1
    while True:
        if f(fy(n),fx(n)) > f(b,a):
            break
        n = n + 1
    k = int(a/(a*fy(n)-b*fx(n)))+1
    return k * fy(n)
