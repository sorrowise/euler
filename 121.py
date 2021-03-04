# approach 1, time cost = 490 µs ± 8.63 µs

import sympy as sp
from math import prod,factorial

def main(n=15):
    x = sp.var('x')
    expr = prod([(x+i) for i in range(1,n+1)])
    p = sp.Poly(expr)
    res = factorial(n+1)//sum(p.coeffs()[:n//2+1])
    return res

# approach 2, time cost = 1.01ms

from fractions import Fraction as f
from functools import lru_cache
from math import factorial

@lru_cache(maxsize=None)
def prob(n,k):
    if k == 0:
        return f(1,n+1)
    elif n == k:
        return f(1,factorial(n+1))
    else:
        return prob(n-1,k)*f(n,n+1)+prob(n-1,k-1)*f(1,n+1)

def main(n=15):
    p = sum([prob(n,i) for i in range(n//2+1,n)])
    return 1//p
