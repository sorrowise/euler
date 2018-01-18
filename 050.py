# time cost = 329 µs

from sympy import sieve
from sympy.ntheory import isprime

def main(upbound=3943):
    primes = list(reversed(list(sieve.primerange(1,upbound))))
    for d in range(len(primes)-1,0,-1):
        for start in range((len(primes)-d+1)):
            res = sum(primes[start:start+d])
            if isprime(res):
                return res
