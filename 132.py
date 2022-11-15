# time cost = 242 ms ± 488 µs

from sympy import primerange

def main(N=10**9,k=40):
    primes = [p for p in primerange(7,200000) if pow(10,N,p)==1]
    return sum(primes[:k])
