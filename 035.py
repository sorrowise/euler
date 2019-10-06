# time cost = 119 ms ± 4.07 ms

from sympy import sieve,isprime

def rotate_set(num):
    s = str(num)
    res = {num}
    for i in range(len(s)):
        new = s[1:] + s[0]
        res.add(int(new))
        s = new
    return res

def main():
    primes = set(sieve.primerange(100,1e6))
    digitset = {'1','3','7','9'}
    res_set = {i for i in primes if set(str(i))<=digitset}
    for ele in res_set:
        x = rotate_set(ele)
        for i in x:
            if isprime(i) == False:
                res_set = res_set-x
                break
    return len(res_set)+13
