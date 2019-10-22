# time cost = 146 µs ± 791 ns

def main(p=1000):
    for a in range(1,p//3):
        n,d = p**2-2*p*a,2*p-2*a
        if n % d == 0:
            b = n/d
            c = p-a-b
            return int(a*b*c)
