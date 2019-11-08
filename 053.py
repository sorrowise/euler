# time cost = 997 µs ± 5.72 µs

from math import factorial as fac

def comb_num(n,k):
    num = fac(n)/(fac(n-k)*fac(k))
    return num

def main():
    count = 0
    for r in range(23,101):
        for c in range(1,r//2):
            if comb_num(r,c) > 10**6:
                count += (r - 2*c + 1)
                break
    return count
