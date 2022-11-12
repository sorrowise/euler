# time cost = 10.4 s ± 291 ms

from itertools import permutations,product
from sympy import isprime
from sympy.utilities.iterables import multiset_partitions

def main():
    cnt = 0
    for pt in multiset_partitions([str(x) for x in range(1,10)]):
        for perm in product(*(permutations(x) for x in pt)):
            if all(isprime(int("".join(x))) for x in perm):
                cnt += 1
    return cnt
