# time cost = 885 µs ± 9.93 µs

from math import log10

def main(N=1000):
    c,n,d = 0,1,1
    for i in range(N):
        n,d = 2 * d + n,d + n
        if int(log10(n)) > int(log10(d)):
            c += 1
    return c
