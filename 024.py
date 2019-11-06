# time cost = 280 ns ± 1.51 ns

from math import factorial as fac
from functools import lru_cache

@lru_cache(maxsize=128)
def nth_lexi_perm(n,s):
    if len(s) == 1:
        return s
    else:
        q,r = divmod(n,fac(len(s)-1))
        return (s[q] + nth_lexi_perm(r,s[:q]+s[q+1:]))

def main(n=10**6,s='0123456789'):
    return nth_lexi_perm(n-1,s)
