from sympy import sieve

def is_truncprime(x,lst):
    s = str(x)
    for d in range(1,len(s)):
        if int(s[d:]) not in lst or int(s[:d]) not in lst:
            return False
    return True

def sum_of_truncprimes():
    upbound = 1e6
    res = []
    while len(res) < 15:
        primes = list(sieve.primerange(1,upbound))
        odd_set = {'1','3','7','9'}
        primes_filter = [x for x in primes if set(str(x))-odd_set == set() or x<100]
        res = [x for x in primes_filter if is_truncprime(x,primes_filter)]
        upbound += 10000
        return sum(res) - sum([2,3,5,7])
