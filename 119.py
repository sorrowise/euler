# time cost = 2.84 ms ± 14.9 µs

def main(k=30):
    arr = []
    for b in range(1,100):
        for p in range(1,10):
            n = b ** p
            if n > 10:
                ds = sum([int(x) for x in str(n)])
                if ds == b:
                    arr.append(n)
    return sorted(arr)[k-1]
