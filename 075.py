from math import gcd

# time cost = 823 ms ± 3.39 ms

def main(N=1500000):
    dt,limit = {},int((N//2)**0.5)+1
    for m in range(2,limit):
        for n in range(1,m):
            if (m+n)%2 == 1 and gcd(m,n) == 1:
                p,k = 2*m*(m+n),1
                while k*p <= N:
                    if k*p in dt:
                        dt[k*p] += 1
                    else:
                        dt[k*p] = 1
                    k += 1
    return len([x for x in dt.values() if x==1])
