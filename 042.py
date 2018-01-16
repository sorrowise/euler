with open('euler/ep42.txt','r') as f:
    data = f.read().replace('"',"").split(',')

def alphabet(word):
    alpha = lambda s : ord(s) - ord('A') + 1
    res = sum([alpha(x) for x in word])
    return res

word_value = [alphabet(x) for x in data]
triangle_num = [n*(n+1)//2 for n in range(1,25)]
len([x for x in word_value if x in triangle_num])
