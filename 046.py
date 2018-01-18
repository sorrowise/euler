# time cost = 711ms

from math import sqrt
from sympy.ntheory import isprime

def is_square(x):
    sq = round(sqrt(x))
    if sq**2 == x:
        return True
    return False

def main():
    odd_comp = 35
    while True:
        if not isprime(odd_comp):
            primes = list(sieve.primerange(1,odd_comp))
            if all(not is_square(x) for x in [(odd_comp-x)/2 for x in primes]):
                return odd_comp
        odd_comp += 2
