# time cost = 40.2 ms ± 412 µs

def main(N=1000):
        a,b,n = 1,1,1
        while True:
            n += 1
            a,b = b,a+b
            if len(str(a)) == N:
                return n
