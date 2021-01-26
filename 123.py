# time cost = 358 ms ± 3.45 ms

from sympy import nextprime

def main(N=10**10):
    n,p = 7037,71059
    while True:
        np = nextprime(p,2)
        n = n + 2
        r = 2*n*np
        if r > N:
            return n
        else:
            p = np
