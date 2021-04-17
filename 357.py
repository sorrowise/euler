# time cost = 32.9 s ± 120 ms

from sympy import isprime
import numpy as np

def prime_sieve(n):
    sieve = np.ones(n//3+(n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[((k*k)//3)::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def is_valid(n):
    u = int(n**0.5) + 1
    for i in range(2,u):
        if n % i == 0:
            if not isprime(i+n//i):
                return False
    return True 

def main(N=10**8):
    arr = prime_sieve(N) - 1
    return arr[np.vectorize(is_valid)(arr)].sum()
