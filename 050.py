from sympy import sieve
from sympy.ntheory import isprime

def main():
    primes = list(sieve.primerange(1,3943))
    for d in range(len(primes)-1,0,-1):
        for start in range((len(primes)-d+1)):
            if isprime(sum(primes[start:start+d])):
                return sum(primes[start:start+d])
