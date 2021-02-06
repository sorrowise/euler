# time cost = 1.51 s ± 5.57 ms

from sympy import primerange,primepi

def main(N=10**8):
    c =  0
    u = int(N**0.5)
    primes = primerange(1,u+1)
    for n,p in enumerate(primes):
        c += primepi(N//p)-n
    return c
