# time cost = 2.77 s ± 5.66 ms

from itertools import product
from sympy import primerange

def main(N=5*10**7):
    ans = set()
    square_limit = int(N**(1/2))+1
    cube_limit = int(N**(1/3))+1
    fourth_power_limit = int(N**(1/4))+1
    for i,j,k in product(primerange(1,square_limit),primerange(1,cube_limit),primerange(1,fourth_power_limit)):
        p = i**2 + j**3 + k**4
        ans.add(p)
    return len({x for x in ans if x<N})