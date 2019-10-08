# time cost = 2.5 ms ± 13 µs

def make_palindrome(x):
    s = str(x)
    p1 = s + s[::-1]
    p2 = s + s[:-1][::-1]
    return int(p1),int(p2)

def main():
    is_palindrome = lambda x : x[-1]!=0 and x == x[::-1]
    res = 0
    for i in range(1,1000):
        p1,p2 = make_palindrome(i)
        p1_base2,p2_base2 = bin(p1)[2:],bin(p2)[2:]
        if is_palindrome(p1_base2):
            res = res + p1
        if is_palindrome(p2_base2):
            res = res + p2
    return res
