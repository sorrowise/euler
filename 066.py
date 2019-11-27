# time cost = 17.2 ms ± 50.2 µs

def pell_equation(D):
    a0 = int(D**0.5)
    a1 = int(2*a0/(D-a0**2))
    seq,P,Q = [a0,a1],[a0,a1*a0+1],[1,a1]
    m,d = a0,D-a0**2
    while seq[-1] != 2*a0:
        m = d*seq[-1]-m
        d = (D-m**2)//d
        seq.append(int((a0+m)/d))
        P.append(seq[-1]*P[-1]+P[-2])
        Q.append(seq[-1]*Q[-1]+Q[-2])
    if (len(seq)-1) % 2 == 0:
        return (P[-2],Q[-2])
    else:
        return (P[-2]**2+Q[-2]**2*D,2*P[-2]*Q[-2])

def main(N=1000):
    dt = {}
    for i in range(8,N+1):
        if int(i**0.5)**2 == i:
            continue
        else:
            dt[i] = pell_equation(i)[0]
    return max(dt,key=dt.get)
