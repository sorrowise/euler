# time cost = 490 µs ± 8.63 µs

import sympy as sp
from math import prod,factorial

def main(n=15):
    x = sp.var('x')
    expr = prod([(x+i) for i in range(1,n+1)])
    p = sp.Poly(expr)
    res = factorial(16)//sum(p.coeffs()[:8])
    return res
