# time cost = 4.71 ms ± 3.86 µs

from functools import reduce

def main():
    with open('euler/ep08.txt','r') as f:
        data = ''
        for line in f.readlines():
            data = data + line.strip()
    res = []
    for i in range(988):
        sub = [int(x) for x in data[i:i+13]]
        prod = reduce(lambda x,y:x*y, sub)
        res.append(prod)
    return max(res)
