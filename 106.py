# time cost = 6.35 µs ± 191 ns

from math import factorial as fac

def comb_num(n,k):
    num = fac(n)//(fac(n-k)*fac(k))
    return num

def main(N=12):
    res = 0
    for i in range(1,N//2+1):
        res += comb_num(N,2*i)*(comb_num(2*i,i)//2-comb_num(2*i,i)//(i+1))
    return res
