# time cost = 2.22 s ± 15.5 ms

from sympy.ntheory.modular import crt
from math import log10,ceil
from sympy import primerange

def smallest_number(p1,p2):
    m = pow(10,ceil(log10(p1)))
    u,v = [0,p1],[p2,m]
    res = crt(v,u)[0]
    return res

def main(N=10**6+4):
    res = 0
    primes = list(primerange(5,N))
    for i in range(len(primes)-1):
        res += smallest_number(primes[i],primes[i+1])
    return res
