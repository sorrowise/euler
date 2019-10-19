# time cost = 6.7 ms ± 709 µs

from sympy import isprime,primerange,nextprime

def primesum_below_N(N):
    start = 2
    arr = [start]
    while True:
        nextp = nextprime(start)
        arr.append(nextp)
        if sum(arr)>=N:
            return arr[:-1]
        start = nextp

def main(N=10**6):
    primes = primesum_below_N(N)
    length = len(primes)
    for d in range(length-1,0,-1):
        for start in range((length-d+1)):
            res = sum(primes[start:start+d])
            if isprime(res):
                return (primes[start],d,res)
