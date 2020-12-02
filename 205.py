# approach 1, time cost = 101 ms ± 484 µs

from itertools import product
from collections import Counter

def dice_values_sum_ways(sides,number):
    arrangement = product(range(1,sides+1),repeat=number)
    sum_of_values = [sum(x) for x in arrangement]
    c = Counter(sum_of_values)
    return dict(c)

def main():
    beats = 0
    total = (4**9) * (6**6)
    pw = dice_values_sum_ways(4,9)
    cw = dice_values_sum_ways(6,6)
    for k1,v1 in pw.items():
        for k2,v2 in cw.items():
            if k1 > k2:
                beats += (v1*v2)
    return round(beats/total,7)

# appraoch 2, time cost = 3.88 ms ± 53.3 µs

from scipy.special import comb

def numbers_of_ways(m,n,p):
    up = int((p-m)/n)+1
    seq = [(-1)**j * comb(m,j) * comb(p-n*j-1,m-1) for j in range(up)]
    return sum(seq)

def prob():
    beats = 0
    total = (4**9) * (6**6)
    pw = {i:numbers_of_ways(9,4,i) for i in range(9,37)}
    cw = {i:numbers_of_ways(6,6,i) for i in range(6,37)}
    for k1,v1 in pw.items():
        for k2,v2 in cw.items():
            if k1 > k2:
                beats += (v1*v2)
    return round(beats/total,7)
