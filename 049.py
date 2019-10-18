# time cost = 3.8 ms ± 549 µs

from sympy import isprime,primerange

def main():
    primes = primerange(1000,10000)
    for p in primes:
        if p != 1487:
            a = p + 3330
            b = p + 6660
            if isprime(a) and isprime(b) and set(str(p))==set(str(a))==set(str(b)):
                return str(p) + str(a) + str(b)
