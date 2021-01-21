# time cost = 25.1 µs ± 56.2 ns

def main(U=10**9):
    x,y = 7,4
    p_sum = 0
    while True:
        a1,a2 = (2*x+1)/3,(2*x-1)/3
        s1,s2 = (a1+1)*y/2,(a2-1)*y/2
        p1,p2 = (3*a1+1),(3*a2-1)
        if (p1<=U) and (a1%1==0) and (s1%1==0):
            p_sum += p1
        if (p2<=U) and (a2%1==0) and (s2%1==0):
            p_sum += p2
        if (p1>U) and (p2>U):
            return p_sum
        else:
            x,y = 2*x+3*y,x+2*y
