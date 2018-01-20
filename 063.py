# ans = 49, time cost = 168 µs

def diff(x):
    d = [n-len(str(x**n)) for n in range(1,25)]
    res = [x for x in d if x==0]
    return len(res)

def main():
    return sum([diff(x) for x in range(1,10)])
