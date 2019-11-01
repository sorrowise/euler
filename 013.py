# time cost = 159 µs ± 858 ns

def main():
    large_sum = sum(map(int,open('data/ep13.txt')))
    ans = str(large_sum)[:10]
    return ans
