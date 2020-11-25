# time cost = 4.89 µs ± 19 ns

def reversible_numbers(d):
    r = d % 4
    if r == 0 or r == 2:
        return 20*30**(d//2-1)
    elif r == 3:
        return 100*(500)**((d-3)//4)
    else:
        return 0

def main():
    ans = sum([reversible_numbers(x) for x in range(2,10)])
    return ans
