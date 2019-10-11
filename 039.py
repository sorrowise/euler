# time cost = 60.1 ms ± 626 µs

def number_of_solution(p):
    num = 0
    for a in range(1,p//3):
        if (p**2-2*p*a)%(2*p-2*a) == 0:
            num += 1
    return num

def main(n=1000):
    d = {p:number_of_solution(p) for p in range(2,n+1,2)}
    ans = max(d,key=d.get)
    return ans
