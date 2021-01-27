# time cost = 22.6 µs ± 87 ns

def main():
    res = 0
    tdp = lambda x: (x**11+1)//(x+1)
    arr = [tdp(x) for x in range(1,11)]
    diff = lambda arr:[x-y for x,y in zip(arr[1:],arr[:-1])]
    for _ in range(10):
        res += sum(arr)
        arr = diff(arr)
    return res
