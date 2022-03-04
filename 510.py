# time cost = 57.4 s ± 3.32 s

from math import gcd

def triplets(u,v):
    rc = (u*v)**2
    ra = ((u+v)*u)**2
    rb = ((u+v)*v)**2
    return rc,ra,rb

def main(n=10**9):
    res = 0
    u = int(((1+4*n**0.5)**0.5-1)/2)
    for j in range(1,u+1):
        for i in range(1,j+1):
            k = 1
            if gcd(i,j) == 1:
                rc,ra,rb = triplets(i,j)
                while k*rb <= n:
                    res += k*(rc+ra+rb)
                    k += 1
    return res
