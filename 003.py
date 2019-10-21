# time cost = 238 µs ± 789 ns

def main(n=600851475143):
    i = 2
    while i * i < n:
        while n%i == 0:
            n /= i
        i += 2 if i>2 else 1
    return n
