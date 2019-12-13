# time cost = 2ms

from functools import lru_cache

@lru_cache(maxsize=2048)
def partition(i,j):
    if i == 1 or j == 1:
        return 1
    elif i <= j:
        return partition(i,i-1)+1
    else:
        return partition(i,j-1) + partition(i-j,j)

def main(N=100):
    return partition(N,N-1)
