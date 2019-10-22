# approach 1, time complexity = O(n^2)

from math import gcd
from functools import reduce

def lcm(n):
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, range(1,n+1))

# approach 2, time complexity = O(nlog(n))

from sympy import primerange
from math import sqrt,log,floor

def main(n=20):
    primes = list(primerange(1,n))
    i,ans = 0,1
    while primes[i] < sqrt(n):
        e = floor(log(n)/log(primes[i]))
        ans *= (primes[i])**e
        i += 1
    for p in primes[i:]:
        ans *= p
    return ans
