# time cost = 127 ms ± 1.09 ms

from sympy import factorint

def number_of_divisor(n):
    d = factorint(n)
    res = 1
    for i in d:
        res *= (d[i]+1) if i%2==1 else d[i]
    return res

def main(): 
    n = 7
    nd,nnd = number_of_divisor(n),number_of_divisor(n+1)
    while nd*nnd <= 500:
        n += 1
        nd,nnd = nnd,number_of_divisor(n+1)
    return n*(n+1)//2
