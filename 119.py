# time cost = 2.68 ms ± 16.7 µs per

def main(k=30):
    arr = []
    for b in range(2,100):
        for p in range(2,10):
            n = b ** p
            if n > 10:
                ds = sum([int(x) for x in str(n)])
                if ds == b:
                    arr.append(n)
    return sorted(arr)[k-1]
