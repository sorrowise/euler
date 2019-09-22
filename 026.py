# time cost = 11.7 ms ± 188 µs

from math import gcd
from sympy import isprime

def repeat_num(n):
    rem = [1]
    while True:
        rem.append(10*rem[-1]%n)
        if rem[-1] == 0:
            return 0
        elif rem[-1] in rem[:-1]:
            return (len(rem)-1)

def main(n=1000):
    for i in range(n,1,-1):
        if gcd(10,i) == 1 and isprime(i):
            rep_num = repeat_num(i)
            if rep_num == i-1:
                return i     
