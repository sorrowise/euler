# -*- coding: utf-8 -*-

from sympy import sieve
from math import log,ceil

def nth_prime(n):
    up_bound = ceil((log(n)+log(log(n))) * n)
    primes = list(sieve.primerange(1,up_bound))
    return primes[n-1]

print nth_prime(10001)
