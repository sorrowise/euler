# time cost = 456 ms ± 4.23 ms

from math import log10

def fib_top_digits(k):
    phi = (1+5**0.5)/2
    d = k*log10(phi) - 0.5*log10(5)
    res = int(pow(10,d-int(d)+8))
    return res

def main(N=10**9):
    is_pandigital = lambda n:set(str(n)) == set('123456789')
    a,b,k = 1,1,2
    while True:
        a,b = b,(a+b)%N
        k = k + 1
        if is_pandigital(b) and is_pandigital(fib_top_digits(k)):
            return k
