# time cost =  69 µs ± 1 µs

def kd(n):
    ub = lambda n : 9*sum([x*10**(x-1) for x in range(1,n+1)])
    i = 1
    while ub(i)<n:
        i += 1
    return i,ub(i-1)

def d(n):
    if n == 1:
        return 1
    elif n > 1:
        k,u = kd(n)
        m = (n-u) // k
        r = (n-u) % k
        t = 10**(k-1) + m + 1
        dn = int(str(t)[r-1])
        return dn

def main():
    n = [10**x for x in range(7)]
    ans = 1
    for i in n:
        ans *= d(i)
    return ans
