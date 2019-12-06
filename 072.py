# time cost = 225 ns ± 0.296 ns

from functools import lru_cache

@lru_cache(maxsize=2048)
def sum_of_euler_phi(n):
    if n == 1:
        return 1
    else:
        return n*(n+1)//2 - sum([sum_of_euler_phi(n//i) for i in range(2,n+1)])

def main(N=10**6):
    return sum_of_euler_phi(N)-1
