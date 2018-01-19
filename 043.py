# ans = 16695334890, time cost = 103.166 s

from itertools import permutations as p
from operator import add
from functools import reduce
from numpy import array

def main():
    f = lambda tp : reduce(add,(str(x) for x in tp))
    pandigts = [f(x) for x in list(p(range(10),10))][362880:]
    myint = lambda x : int(x) if x[0]!='0' else int(x[1:])
    res = 0
    denominator = array([2,3,5,7,11,13,17])
    for pd in pandigts:
        nominator = array([myint(pd[x:x+3]) for x in range(1,8)])
        if all(nominator%denominator == 0):
            res += int(pd)
    return res
