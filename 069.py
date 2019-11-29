# time cost = 6.91 ms ± 154 µs

from sympy import prime

def main(N=10**6):
    i,prod,arr = 1,1,[]
    while prod <= N:
        prod *= prime(i)
        arr.append(prod)
        i += 1
    return arr[-2]
