# time cost = 42.1 ms ± 549 µs

def jarvis_sqrt_sum(n,prec=100):
    a,b = 5*n,5
    while len(str(b)) <= prec+3:
        if a >= b:
            a,b = a-b,b+10
        else:
            a,b = a*100,(b-b%10)*10+b%10
    return sum([int(x) for x in str(b)[:100]])

def main():
    numbers = set(range(2,100))-{x**2 for x in range(2,10)}
    ans = 0
    for i in numbers:
        ans += jarvis_sqrt_sum(i)
    return ans
