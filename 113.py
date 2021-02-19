# time cost = 8.51 µs ± 116 ns

from math import factorial as fac

def comb_num(n,k):
    num = fac(n)//(fac(n-k)*fac(k))
    return num

def main(d=100):
    res = comb_num(d+9,9)+comb_num(d+10,10)-10*d-2
    return res
