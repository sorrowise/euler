# time cost = 225 ns ± 0.296 ns

from functools import lru_cache

def number_theory_block(f,n,i=1):
    ans = 0
    while i <= n:
        j = n//(n//i)
        ans += (j-i+1)*f(n//i)
        i = j + 1
    return ans

@lru_cache(maxsize=2048)
def sum_of_euler_phi(n):
    if n == 1:
        return 1
    else:
        return n*(n+1)//2 - number_theory_block(sum_of_euler_phi,n,2)

def main(N=10**6):
    return sum_of_euler_phi(N)-1
