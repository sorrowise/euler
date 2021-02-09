# approach 1, time cost = 583 ns ± 2.65 ns

from functools import lru_cache

@lru_cache(maxsize=None)
def f(n,m):
    if n < m:
        return 1
    else:
        return f(n-m,m)+f(n-1,m)

def main(n=50):
    return f(n,2)+f(n,3)+f(n,4)-3

# approach 2, time cost = 426 µs ± 3.03 µs

from scipy.special import comb

def replaced_ways(n,m):
    w = 0
    for k in range(1,n//m+1):
        t = k + n - k*m
        w += comb(t,k)
    return w

def main(n=50,length=[2,3,4]):
    ways = [replaced_ways(n,x) for x in length]
    return sum(ways)
