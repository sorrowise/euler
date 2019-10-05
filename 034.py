# time cost = 2.22 s ± 3.31 ms

from math import factorial

def main():
    fac_dict = {str(n):factorial(n) for n in range(10)}
    res = 0
    for i in range(10,2177282):
        if sum([fac_dict[x] for x in str(i)]) == i:
            res += i
    return res
