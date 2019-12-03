# time cost = 49.2 ms ± 678 µs

from sympy import primerange

def main():
    is_permutation = lambda x,y : "".join(sorted(str(x))) == "".join(sorted(str(y)))
    primes = list(primerange(2000,4000))
    dt = {(x*y,(x-1)*(y-1)):((x*y)/((x-1)*(y-1))) for x in primes for y in primes if 1<x*y<10**7}
    for n,phi_n in sorted(dt,key=dt.get):
        if is_permutation(n,phi_n):
            return n
