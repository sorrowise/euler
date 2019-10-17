# time cost = 19.7 ms ± 199 µs

from math import sqrt
from sympy import isprime

def exist(x):
    limit = int(sqrt((x-1)/2))
    for i in range(1,limit+1):
        if isprime(x-2*i**2):
            return True
    return False

def main():
    i = 35
    while True:
        if not isprime(i) and not exist(i):
            return i
        i += 2
