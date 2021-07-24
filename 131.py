# time cost = 8.71 ms ± 878 µs

from sympy import isprime

def main(N=576):
    c = 0
    for i in range(1,N+1):
        if isprime(3*i**2+3*i+1):
            c += 1
    return c
