# time cost = 197 ms ± 1.18 ms

from sympy import primerange
from math import log,ceil

def main(n=10001):
    upper_bound = ceil((log(n)+log(log(n))) * n)
    primes = list(primerange(1,upper_bound))
    return primes[n-1]
