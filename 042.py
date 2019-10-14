# time cost = 5.08 ms ± 8.23 µs

from math import sqrt

def alphabet(word):
    alpha = lambda s : ord(s) - ord('A') + 1
    res = sum([alpha(x) for x in word])
    return res

def main():
    with open('euler/ep42.txt','r') as f:
        data = f.read().replace('"',"").split(',')
    word_value = [alphabet(x) for x in data]
    res = [x for x in word_value if sqrt(1+8*x)%2==1]
    return len(res)
