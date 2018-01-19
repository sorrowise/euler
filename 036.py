# ans = 872187, time cost = 878ms

def main():
    is_palindrome = lambda x : str(x) == str(x)[::-1]
    res = sum([x for x in range(1,10**6) if is_palindrome(x) and is_palindrome(int(bin(x)[2:]))])
    return res
