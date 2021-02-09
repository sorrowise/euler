# time cost = 16.9 µs ± 82.7 ns

def main(n=50):
    arr = [1,2,4,8]
    for _ in range(n-4):
        arr.append(sum(arr[-4:]))
    return arr[-1]
