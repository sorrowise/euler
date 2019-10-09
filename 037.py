# time cosst = 76.2 ms ± 249 µs

from sympy import isprime,sieve

def is_twoside_truncatable_prime(x):
    s = str(x)
    for i in range(1,len(s)):
        if not isprime(int(s[i:])) or not isprime(int(s[:i])):
            return False
    return True

def main():
    num,ans = 0,0
    for i in sieve.primerange(10,1e6):
        if i < 100 and is_twoside_truncatable_prime(i):
            num += 1
            ans += i
        elif i>=100:
            s = str(i)
            cond1 = (s[0]=='3' or '7') and (s[-1]=='3' or '7')
            cond2 = set(s)<={'1','3','7','9'}
            if cond1 and cond2 and is_twoside_truncatable_prime(i):
                num += 1
                ans += i
        if num>=11:
            return ans
