# approach 1, time cost = 140 ns ± 11.8 ns

from functools import lru_cache

@lru_cache(maxsize=128)
def path(x,y):
    if x == 0 or y == 0:
        return 1
    else:
        return path(x-1,y) + path(x,y-1)

# approach 2, time cost = 1.76 µs ± 83.9 ns

from math import factorial as fac

def comb_num(n,k):
    num = fac(n)//(fac(n-k)*fac(k))
    return num

def main(n,k):
    return comb_num(n+k,k)
