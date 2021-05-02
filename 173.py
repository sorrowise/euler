# time cost = 45.8 µs ± 293 ns

def main(N=10**6):
    side = N//4
    u = int(side**0.5) + 1
    res = sum((side//i-i for i in range(1,u)))
    return res
