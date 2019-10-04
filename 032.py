# time cost = 49.6 ms ± 443 µs

def main():
    res = set()
    for i in range(1,100):
        start = 1234 if i <=9 else 123
        for j in range(start,10000//i):
            s = str(i) + str(j) + str(i*j)
            if len(s) == 9 and set(s) == set('123456789'):
                res.add(i*j)
    return sum(res)
