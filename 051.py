# time cost = 355 ms ± 1.51 ms

from sympy import nextprime,isprime
from collections import Counter

def is_replacable_prime(n):
    s = str(n)
    count = Counter(s)
    num,d = count.most_common(1)[0]
    if d == 3 and num in set('012'):
        k = 1
        for j in range(int(num)+1,10):
            new = s.replace(num,str(j))
            if isprime(int(new)):
                k += 1
        if k == 8:
            return True
    return False

def main():
    n = 1001
    while True:
        p = nextprime(n)
        if is_replacable_prime(p):
            return p
        else:
            n = p
