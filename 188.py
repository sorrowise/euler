# time cost = 31.9 µs ± 78.6 ns

def main(b=1777,e=1855,m=10**8):
    res,phis = 1,[m]
    while m != 1:
        m = totient(m)
        phis.append(m)
    for phi in reversed(phis):
        res = pow(b,res,phi)
    return res
