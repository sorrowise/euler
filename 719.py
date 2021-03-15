from functools import lru_cache

def ndigits(n):
    res = len(str(n))
    return res

@lru_cache(maxsize=2048)
def f(n,s):
    if n <= s:
        return n == s
    else:
        for i in range(1,ndigits(n)):
            if f(n % (10**i),s-n//(10**i)):
                return True
        return False

def main(N=10**12):
    res = 0
    for i in range(1,int(N**0.5)+1):
        if i%9 == 0 or i%9==1:
            sq = i**2
            if f(sq,i):
                res += sq
    return res
