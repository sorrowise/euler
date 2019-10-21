# time cost = 2.75 µs ± 75.2 ns

def main(N=4e6):
    a,b = 2,8
    arr = [a,b]
    while True:
        a,b = b,4*b+a
        arr.append(b)
        if b > N:
            return sum(arr[:-1])
