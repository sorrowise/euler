# -*- coding: utf-8 -*-

r = range(999,99,-1)
is_palindrome = lambda x : str(x) == str(x)[::-1]
print(max([i*j for i in r for j in r if is_palindrome(i*j)]))
