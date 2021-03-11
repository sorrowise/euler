# time cost = 271 µs ± 3.42 µs

def s(k,r,m=10**9+7):
    res = ((r+1)*(r+2)//2+5)*pow(10,k,m)-9*k-6-r
    return res

def main(n=90):
    fib = [0,1]
    for _ in range(n-1):
        fib.append(sum(fib[-2:]))
    res = [s(*divmod(fib[i],9)) for i in range(2,n+1)]
    return sum(res)%(10**9+7)
