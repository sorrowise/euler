# ans = 153, time cost = 51.4ms

from fractions import Fraction as f
from math import log10

def main():
    lst = [0]*1000
    lst[0] = f(1,1)
    num = 0
    for i in range(1,1000):
        lst[i] = 1 + 1/(1+lst[i-1])
        n_digits = int(log10(lst[i].numerator)) + 1
        d_digits = int(log10(lst[i].denominator)) + 1
        if n_digits > d_digits:
            num += 1
    return num

print(main())
