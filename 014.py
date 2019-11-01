# time cost = 1.26 s ± 105 ms

def main(N=10**6):
    d = {}
    for x in range(2,N):
        i = x
        n = 0
        while x != 1:
            if x < i:
                n = n + d[x]
                break
            elif x % 2 == 0:
                x = x // 2
                n += 1
            else:
                x = (3*x+1) // 2
                n += 2
        d[i] = n
    return max(d,key=d.get)
