# time cost = 29.6s

from sympy import primerange

def legendre(n, p):
    exponent = 0
    while n > 0:
        n //= p
        exponent += n
    return exponent

def main(n=2000_0000, k=1500_0000):
    total_sum = 0

    for p in primerange(1,n):
        exponent = legendre(n, p) - legendre(k, p) - legendre(n - k, p)
        total_sum += exponent * p

    return total_sum
