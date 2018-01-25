# ans = 510510, time cost = 21.4 µs

from sympy import sieve
from operator import mul
from functools import reduce

def main():
    lst = list(sieve.primerange(1,25))
    prod = lambda x : reduce(mul,x)
    index = 1
    while prod(lst[:index])<10**6:
        index += 1
    return prod(lst[:index-1])

print(main())

