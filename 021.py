# time cost = 206 ms ± 2.44 ms

from sympy import factorint

def sum_of_divisors(n):
    divs = factorint(n)
    res = 1
    for p in divs:
        res *= (p**(divs[p]+1)-1)//(p-1)
    return res-n

def main(n=10000):
    arr = []
    for i in range(2,n+1):
        a = sum_of_divisors(i)
        if a != i and sum_of_divisors(a) == i:
            arr.append(i)
    return sum(arr)  
