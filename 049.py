# ans = 296962999629, time cost = 3.18 ms

from sympy import sieve

def main():
    primes = list(sieve.primerange(1488,10000))
    for p in primes:
        a = p + 3330
        b = p + 6660
        if a in primes and b in primes and set(str(p))==set(str(a))==set(str(b)):
            return str(p) + str(a) + str(b)
