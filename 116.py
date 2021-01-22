# time cost = 426 µs ± 3.03 µs

from scipy.special import comb

def replaced_ways(n,length):
    w = 0
    for k in range(1,n//length+1):
        t = k + n - k*length
        w += comb(t,k)
    return w

def main(n=50,length=[2,3,4]):
    ways = [replaced_ways(n,x) for x in length]
    return sum(ways)
