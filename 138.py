# time cost = 6.96 µs ± 23.6 ns

def main(N=12):
    n,res = 0,0
    x,y = 38,17
    while n < N:
        b1,b2 = 2*x+4,2*x-4
        if b1%5 == 0 or b2%5==0:
            res += y
        x,y = 9*x+20*y,4*x+9*y
        n += 1
    return res
