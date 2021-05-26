# It has not been completely resolved and needs to be further modified

from math import prod,log,gcd
from functools import lru_cache
from sympy.ntheory.modular import crt

def v(n):
    u = int(log(n,5))
    return sum([n//(5**i) for i in range(1,u+1)])

@lru_cache(maxsize=None)
def A(n,m=3125):
    if n < m:
        return prod([x for x in range(1,n+1) if gcd(x,5)==1])
    else:
        q,r = divmod(n,m)
        return ((-1)**q*A(r))

@lru_cache(maxsize=None)
def F(n,m=3125):
    td = {1: 1, 2: 2, 3: 6, 4: 24, 5: 12, 6: 72, 7: 504, 8: 907, 9: 1913, 10: 1913}
    if n <= 10:
        return td[n]
    else:
        q,r = divmod(n,5)
        Q,R = divmod(n,m)
        return (((F(q))*(A(n)))//(pow(5,v(n)-q-v(q),m)*pow(2,v(n)-v(q),m)))%m

def main(n=10**12):
    res = crt([3125,32],[F(n),0])
    return res[0]
