# time cost = 1.51 µs ± 31.6 ns

def main(N=30):
    a,b = 1,2
    for _ in range(N):
        a,b = b,a+b
    return a
