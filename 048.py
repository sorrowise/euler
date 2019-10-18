# time cost = 9.14 ms ± 71.6 µs

def main():
    res = sum([x**x for x in range(1,1001)])
    return (res % 10**10)
