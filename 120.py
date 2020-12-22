# time cost = 617 µs ± 1.28 µs

def main():
    even = [a**2-2*a for a in range(3,1001) if a%2==0]
    odd = [a**2-a for a in range(3,1001) if a%2==1]
    ans = sum(even) + sum(odd)
    return ans
