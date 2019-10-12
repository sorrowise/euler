# time cost =  69 µs ± 1 µs

def get_k_lb(n):
    lower_bound = lambda n : 9*sum([x*10**(x-1) for x in range(1,n+1)])
    i = 1
    while lower_bound(i)<n:
        i += 1
    return i,lower_bound(i-1)

def get_digit(n):
    if n == 1:
        return 1
    elif n > 1:
        k,lb = get_k_lb(n)
        m = (n-lb) // k
        r = (n-lb) % k
        t = 10**(k-1) + m + 1
        dn = int(str(t)[r-1])
        return dn

def main():
    n = [10**x for x in range(7)]
    ans = 1
    for i in n:
        ans *= get_digit(i)
    return ans
