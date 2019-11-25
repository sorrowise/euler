# time cost = 285 ms ± 3.41 ms

def square_root_period(n):
    a0 = int(n**0.5)
    if a0**2 == n:
        return 0
    else:
        a,m,d,arr = a0,0,1,[a0]
        while arr[-1] != 2*a0:
            m = d*a - m
            d = (n - m**2)//d
            a = int((a0+m)/d)
            arr.append(a)
    return len(arr)-1

def main(N=10000):
    c = 0
    for i in range(1,N+1):
        if square_root_period(i) % 2 == 1:
            c += 1
    return c
