# time cost = 2.85 s ± 86.9 ms

import numpy as np

def prime_sieve(n):
    sieve = np.ones(n//3+(n%6==2), dtype=bool)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[((k*k)//3)::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

def main(n=32000000):
    res = 0
    p_squares = set(p*p for p in prime_sieve(n))
    for p in p_squares:
        rp = int(str(p)[::-1])
        if p != rp and rp in p_squares:
            res += p
    return res
