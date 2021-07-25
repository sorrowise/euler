# time cost = 103 ns ± 3.11 ns

from math import log
from sympy import isprime
from functools import lru_cache

@lru_cache(maxsize=None)
def hn(n,f):
    if n == 1:
        return 1
    elif f == 2:
        return int(log(n,2))+1
    elif n < f:
        return hn(n,n)
    elif not isprime(f):
        return hn(n,f-1)
    else:
        return hn(n,f-1)+hn(n//f,f)

def main(n=10**9,f=100):
    return hn(n,f)
