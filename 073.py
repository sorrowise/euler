# approach 1, time cost = 2.97 s ± 6.42 ms

def farey_seq(n=12000):
    b, d = 3, 11999
    ans = 0
    while d!=2:
        ans += 1
        k = int((n + b) / d)
        b, d = d, k * d - b
    return ans


# approach 2, time cost = 101 ns ± 0.171 ns

from functools import lru_cache

def number_theory_block(f,n,i=1):
    ans = 0
    while i <= n:
        j = n//(n//i)
        ans += (j-i+1)*f(n//i)
        i = j + 1
    return ans

def fractions_count(n):
    q,r = divmod(n,6)
    i = 1 if r == 5 else 0
    ans = q*(3*q-2+r)+i
    return ans

@lru_cache(maxsize=2048)
def reduced_fractions_count(n=12000):
    if n == 1:
        return 0
    else:
        return fractions_count(n) - number_theory_block(reduced_fractions_count,n,2)
