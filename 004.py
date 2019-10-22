# time cost = 169 ms ± 402 µs

def main():
    r = range(999,99,-1)
    is_palindrome = lambda x : str(x) == str(x)[::-1]
    ans = max([i*j for i in r for j in r if (i*j)%11==0 and is_palindrome(i*j)])
    return ans
