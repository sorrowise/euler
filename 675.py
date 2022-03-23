from collections import defaultdict

def smallest_prime_factor_sieve(n):
    arr = list(map(lambda x: x if x%2==1 else 2,range(n+1)))
    for i in range(3,int(n**0.5)+1,2):
        if arr[i] == i:
            for j in range(i*i,n+1,i):
                if arr[j] == j:
                    arr[j] = i
    return arr

def prime_factorization_sieve(n):
    spf = smallest_prime_factor_sieve(n)
    def get_factorization(x):
        res = dict()
        while x != 1:
            p = spf[x]
            exp = 1
            x = x // p
            while spf[x] == p:
                exp += 1
                x = x // p
            res.update({p:exp})
        return res
    return [0,1]+[get_factorization(i) for i in range(2,n+1)]

def sf(factors):
    res = 1
    for power in factors.values():
        res *= (2*power+1)
    return res

def main(N=10**7):
    M = 1000000087
    res,ct = 0,defaultdict(int)
    factors = prime_factorization_sieve(N)
    for i in range(1,N):
        for k,v in factors[i+1].items():
            ct[k] += v
        res += (sf(ct) % M)
    return res%M
