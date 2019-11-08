# time cost = 342 ms ± 2.79 ms

from sympy import nextprime,isprime
from collections import Counter

def is_replacable_prime(n):
    count = Counter(str(n))
    most = count.most_common(1)[0]
    if most[1] == 3 and most[0] in set('012'):
        k = 1
        for j in range(int(most[0])+1,10):
            new = str(n).replace(most[0],str(j))
            if isprime(int(new)):
                k += 1
        if k == 8:
            return True
    return False

def main():
    n = 10001
    while True:
        p = nextprime(n)
        if is_replacable_prime(p):
            return p
        else:
            n = p
