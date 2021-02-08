# time cost = 186 ns ± 1.67 ns

from functools import lru_cache

@lru_cache(maxsize=None)
def f(n,m):
    if n < m:
        return 1
    elif n == m:
        return 2
    else:
        return 2*f(n-1,m)-f(n-2,m)+f(n-m-1,m)

def main():
    return f(50,3)
