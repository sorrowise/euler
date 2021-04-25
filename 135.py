# time cost = 1.21 s ± 5.8 ms

from collections import defaultdict

def main(N=10**6):
    res = defaultdict(int)
    for a in range(2,N+1):
        u = min(a,(N+a**2)//(4*a)+1)
        for d in range(a//4+1,u):
            res[a*(4*d-a)] += 1
    return len([k for k,v in res.items() if v==10])
