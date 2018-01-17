# time cost = 860ms

def is_permuted(x):
    multiples = [set(str(x*n)) for n in range(1,7)]
    if all(x==multiples[0] for x in multiples):
        return True
    return False

def main():
    start = 10
    while not is_permuted(start):
        start += 1
    return start
