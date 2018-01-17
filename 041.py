# approach 1, time cost = 1.95s

from sympy import sieve

def is_pandgit(x):
    pandgit_set = {int(x) for x in str(x)}
    if pandgit_set == set(range(1,len(str(x))+1)):
        return True
    return False

max([x for x in list(sieve.primerange(1,7654321)) if is_pandgit(x)])

# approach 2, time cost = 180ms

from functools import reduce
from operator import add
from itertools import permutations
from sympy import sieve

def main():
    number_list = [str(x) for x in range(1,8)]
    res_list = [int(reduce(add,x)) for x in list(permutations(number_list,7))]
    cross_set = set(res_list) & set(sieve.primerange(1234567,7654321))
    return max(cross_set)
