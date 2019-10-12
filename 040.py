# time cost =  36.2 µs ± 433 ns

def get_k_pub(n):
    previous_bound = lambda k : 10**k*(k-1/9)+1/9
    k = 1
    while previous_bound(k)<n:
        k += 1
    return k,int(previous_bound(k-1))

def get_digit(n):
    if n < 10:
        return n
    elif n >= 10:
        k,pub = get_k_pub(n)
        m = (n-pub) // k
        r = (n-pub) % k
        t = 10**(k-1) + m + 1
        dn = int(str(t)[r-1])
        return dn

def main():
    n = [10**x for x in range(7)]
    ans = 1
    for i in n:
        ans *= get_digit(i)
    return ans
