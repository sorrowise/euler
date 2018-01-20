# ans = 249, time cost = 71.5ms

def is_lychrel(x):
    n = 1
    is_palindrome = lambda x : str(x) == str(x)[::-1]
    while True:
        reverse = str(x)[::-1]
        if is_palindrome(x+int(reverse)):
            return False
        else:
            x = int(reverse) + x
            n += 1
            if n > 50:
                return True
            
def main():
    res = len([x for x in range(1,10000) if is_lychrel(x)])
    return res
