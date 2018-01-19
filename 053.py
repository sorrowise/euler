# ans = 4075, time cost = 12.6ms

from math import factorial as fac

def comb_num(n,k):
    num = fac(n)/(fac(n-k)*fac(k))
    return num

def main():
    num = 0
    for n in range(1,101):
        for r in range(2,n):
            if comb_num(n,r) > 1e6:
                num += 1
    return num
