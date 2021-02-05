# time cost = 1.16 s ± 7.57 ms

import numpy as np
from numba import njit

@njit
def number_of_divisors(N):
    nod = np.array([0,1]+[2]*(N-1))
    u = int(N**0.5)
    for i in range(2,u+1):
        nod[i*i] += 1
        for j in range(i+1,N//i+1):
            nod[i*j] += 2
    return nod

def main(N=10**7):
    nod = number_of_divisors(N)
    diff = np.diff(nod)
    res = N - np.count_nonzero(diff)
    return res
