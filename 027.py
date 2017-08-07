# -*- coding: utf-8 -*-

from math import sqrt
from sympy import sieve

def is_prime(n):
    if n<=1:
        return False
    else:
        primes = list(sieve.primerange(1,int(sqrt(n))+1))
        return not [i for i in primes if n%i == 0]

def quad_prime(a,b):
    f = lambda n,a,b : n**2 + a*n + b
    n = 0
    while True:
        if is_prime(f(n,a,b)):
            n = n + 1
        else:
            return n

arr = [x for x in range(-999,1000) if x%2==1]
primes = list(sieve.primerange(1,1001))
res = []
for a in arr:
    for b in primes:
        res.append((a,b,quad_prime(a,b)))
consec_num = [x[2] for x in res]
a,b = res[consec_num.index(max(consec_num))][0:2]
print a*b
