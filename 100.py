# time cost = 5.73 µs ± 59.8 ns

def main(N=10**12):
    b,t = 15,21
    while t < N:
        b,t = 2*t+3*b-2,3*t+4*b-3
    return b
