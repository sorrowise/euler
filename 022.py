# time cost = 246 ms ± 608 µs

def alphabet(word):
    alpha = lambda s : ord(s) - ord('A') + 1
    res = sum([alpha(x) for x in word])
    return res

def main():
    with open('data/ep22.txt','r') as f:
        names = f.read().replace('"',"").split(',')
    sorted_names = sorted(names)
    name_score = lambda word : alphabet(word) * (sorted_names.index(word)+1)
    ans = sum([name_score(word) for word in names])
    return ans
