# ans = 5482660, time cost = 2.34s

from itertools import combinations
from math import sqrt

def is_pantagon(x):
    if (sqrt(24*x+1)+1) % 6 == 0:
        return True
    return False

def main(upbound=3000):
    pantagon = lambda n : n*(3*n-1)/2
    pantagon_list = [pantagon(n) for n in range(1,upbound)]
    combs = list(combinations(pantagon_list,2))
    for x in combs:
        d = abs(x[1]-x[0])
        if is_pantagon(sum(x)) and is_pantagon(d):
            return d   
