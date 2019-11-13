# time cost = 64.8 ms ± 229 µs

def is_lychrel(x):
    is_palindrome = lambda x : str(x) == str(x)[::-1]
    for _ in range(50):
        x += int(str(x)[::-1])
        if is_palindrome(x):
            return False
    return True

def main():
    ans = len([x for x in range(1,10000) if is_lychrel(x)])
    return ans
