# time cost = 997 µs ± 5.72 µs

from math import factorial as fac

def comb_num(n,k):
    num = fac(n)/(fac(n-k)*fac(k))
    return num

def main():
    count = 0
    for n in range(23,101):
        for r in range(1,n//2):
            if comb_num(n,r) > 10**6:
                count += (n - 2*r + 1)
                break
    return count
