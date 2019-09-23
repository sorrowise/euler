# time cost = 2.34 s ± 48 ms

from sympy import isprime

def consecutive_primes(a,b):
    f = lambda n,a,b : n**2 + a*n + b
    n = 0
    while True:
        if isprime(f(n,a,b)):
            n = n + 1
        else:
            return n

def main():
    res = {}
    for a in range(-999,1000,2):
        for b in [x for x in range(-1000,1001) if isprime(x)]:
            res[consecutive_primes(a,b)] = (a,b)
    a,b = res[max(res)]
    return a*b
