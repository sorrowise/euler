# time cost = 2.82 s ± 83.9 ms

from sympy import isprime,primerange
import networkx as nx
from networkx.algorithms.clique import find_cliques

def is_pair_prime(x,y):
    conc = lambda x,y:isprime(int(str(x)+str(y)))
    if x == 3:
        return conc(x,y) and conc(y,x)
    else:
        r = x % 3
        return y%3==r and conc(x,y) and conc(y,x)

def main(N=8400):
    res = []
    primes = list(primerange(3,N))
    index = 0
    for p in primes:
        index += 1
        for i in primes[index:]:
            if is_pair_prime(p,i):
                res.append((p,i))
    G = nx.Graph()
    G.add_edges_from(res)
    ans = [clique for clique in find_cliques(G) if len(clique)==5]
    return min(map(sum,ans))
