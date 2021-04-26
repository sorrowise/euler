# time cost = 1min 30s ± 4.84 s

from collections import defaultdict

def main(N=5*10**7):
    res = defaultdict(int)
    for a in range(2,N+1):
        u = min(a,(N+a**2)//(4*a)+1)
        for d in range(a//4+1,u):
            res[a*(4*d-a)] += 1
    return len([k for k,v in res.items() if v==1])
