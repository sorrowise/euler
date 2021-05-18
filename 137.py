# time cost = 13.2 µs ± 128 ns

def main(N=15):
    arr = []
    x1,y1,x2,y2,x3,y3 = -1,1,1,1,4,2
    u,v = 9,4
    while True:
        x1,y1 = -u+5*v,-v+u
        x2,y2 = u+5*v,v+u
        x3,y3 = 4*u+10*v,4*v+2*u
        target = [(x-1)//5 for x in [x1,x2,x3] if (x-1)%5==0]
        arr += target
        if len(arr) == N:
            return arr[-1]
        else:
            u,v = 9*u+20*v,4*u+9*v
