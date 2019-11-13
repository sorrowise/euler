# time cost = 190 ms ± 515 µs

def main():
    str_sum = lambda y : sum([int(x) for x in str(y)])
    res = max([str_sum(a**b) for a in range(1,100) for b in range(1,100)])
    return res
