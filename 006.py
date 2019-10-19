# time cost = 569 ns ± 45.8 ns

def main(n=100):
    ans = n*(n-1)*(n+1)*(3*n+2)/12
    return int(ans)
