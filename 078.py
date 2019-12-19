# time cost = 14.1 s ± 66.9 ms

def partion_function(n):
    pn = [1,1]
    for i in range(2,n+1):
        k,acc = 1,0
        g1 = lambda k : i - k*(3*k-1)//2
        g2 = lambda k : i - k*(3*k+1)//2
        f = lambda x : pn[x] if x >= 0 else 0
        while g1(k) >= 0:
            acc += (-1)**(k+1)*(f(g1(k))+f(g2(k)))
            k += 1
        pn.append(acc)
    return pn

def main(N=10**6):
    pn = partion_function(55400)
    for i in range(61,len(pn)):
        if pn[i] % N == 0:
            return i
