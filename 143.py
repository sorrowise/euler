# time cost = 253 ms ± 5.44 ms

from math import gcd
from collections import defaultdict

def generate_pairs(N=120000):
    pairs = defaultdict(set)
    for i in range(2,346):
        for j in range(1,i):
            if gcd(i,j) == 1 and (i-j)%3 != 0:
                q,r = 2*i*j+j**2,i**2-j**2
                q,r = max(q,r),min(q,r)
            for k in range(1,N//q+1):
                pairs[k*q].add(k*r)
    return pairs

def main(N=120000):
    res = set()
    pairs = generate_pairs()
    for k,v in pairs.items():
        for q in v:
            if q in pairs:
                for r in (v & pairs[q]):
                    res.add(k+q+r)
    return sum({x for x in res if x<=N})
