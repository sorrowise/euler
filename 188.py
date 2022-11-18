# time cost = 4.21 ms ± 10.7 µs

def main(b=1777,e=1855,m=10**8):
    res = b
    for _ in range(e):
        res = pow(b,res,m)
    return res


# time cost = 4.74 ms ± 9.72 µs

from sympy.ntheory import totient

def main(b=1777,e=1855,m=10**8):
    res = b
    for _ in range(e):
        res = pow(b,res%totient(m),m)
    return res
