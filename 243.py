# time cost = 53.2 ms ± 517 µs

from sympy import prime,primorial
from fractions import Fraction as f
from math import prod

def resilience(n,k=1):
    primes = [prime(i) for i in range(1,n+1)]
    prod_p = prod(primes)
    prod_q = prod([x-1 for x in primes])
    res = f(k*prod_p,k*prod_p-1)*f(prod_q,prod_p)
    return res

def main(target=f(15499,94744)):
    n,k = 1,2
    while resilience(n) > target:
        n = n + 1
    while resilience(n-1,k) > target:
        k = k + 1
    return k*primorial(n-1)
