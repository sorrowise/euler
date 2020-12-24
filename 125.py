# time cost = 224 ms ± 1.35 ms

def is_palindromic(n):
    n = str(n)
    return n == n[::-1]

def main(N=10**8):
    psos = set()
    u = int((N/2)**0.5)
    for i in range(1,u):
        sos = i*i
        while sos < N:
            i += 1
            sos += i*i
            if is_palindromic(sos): 
                psos.add(sos)
    return sum(psos)
