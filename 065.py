# time cost = 30.8 µs ± 113 ns

def main(N=100):
    m,n = 1,2
    for i in range(2,N+1):
        a = 2 * i//3 if i%3==0 else 1
        m,n = n,m+a*n
    return sum(map(int,str(n)))
