# time cost = 642 µs ± 2.22 µs

from sympy.ntheory import n_order

def main(N=10**6):
    n = N + 1
    while True:
        if n % 5 != 0 and n_order(10,9*n)>N:
            return n
        else:
            n = n + 2
