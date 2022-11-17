# time cost = 4.21 ms ± 10.7 µs

def main(b=1777,e=1855,m=10**8):
    res = b
    for _ in range(e):
        res = pow(b,res,m)
    return res
