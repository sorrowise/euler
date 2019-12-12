# approach1, time cost = 60.1 ms ± 626 µs

def number_of_solution(p):
    num = 0
    for a in range(1,p//3):
        if (p**2-2*p*a)%(2*p-2*a) == 0:
            num += 1
    return num

def main(n=1000):
    d = {p:number_of_solution(p) for p in range(2,n+1,2)}
    ans = max(d,key=d.get)
    return ans

# approach 2, time cost = 192 µs ± 844 ns

from math import gcd
from collections import Counter

def max_number_of_solution(N=1000):
    limit,arr = int((N//2)**0.5)+1,[]
    for m in range(2,limit):
        for n in range(1,m):
            if (m+n)%2 == 1 and gcd(m,n) == 1:
                p,k = 2*m*(m+n),1
                while k*p <= N:
                    arr.append(k*p)
                    k += 1
    c = Counter(arr)
    return c.most_common()[0][0]
