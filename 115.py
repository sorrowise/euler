# time cost = 19.8 µs ± 80.8 ns

from functools import lru_cache

@lru_cache(maxsize=None)
def f(n,m):
    if n < m:
        return 1
    elif n == m:
        return 2
    else:
        return 2*f(n-1,m)-f(n-2,m)+f(n-m-1,m)

def main(N=10**6):
    n = 51
    while True:
        w = f(n,50)
        if w > N:
            return n
        else:
            n += 1
