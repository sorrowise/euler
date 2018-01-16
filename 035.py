from sympy import sieve
primes = list(sieve.primerange(10,1e6))

def rotate(s):
    s = str(s)
    lst = []
    for i in range(len(s)):
        new_string = s[1:] + s[0]
        lst.append(int(new_string))
        s = new_string
    return lst

odd_set = {'1','3','7','9'}
primes_filter = [x for x in primes if set(str(x))-odd_set == set()]
len([x for x in primes_filter if all(x in primes_filter for x in rotate(x))])+4
