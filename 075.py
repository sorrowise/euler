# time cost = 1.37 s ± 63.6 ms

from math import gcd
from collections import Counter

def main(N=1500000):
    limit,arr = int((N//2)**0.5)+1,[]
    for m in range(2,limit):
        for n in range(1,m):
            if (m+n)%2 == 1 and gcd(m,n) == 1:
                p,k = 2*m*(m+n),1
                while k*p <= N:
                    arr.append(k*p)
                    k += 1
    c = Counter(arr)
    return len([x for x in c.values() if x==1])
