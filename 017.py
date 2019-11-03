# time cost = 4.31 ms ± 58.6 µs

import pandas as pd

def num_to_words(n):
    if n in words_dict.keys():
        return words_dict[n]
    else:
        if 21<=n<=100:
            ten_digit = n//10*10
            digit = n%10
            return words_dict[ten_digit] + words_dict[digit]
        elif 101<=n<=1000:
            hundred_dict = n//100
            remainder = n%100
            if remainder == 0:
                return words_dict[hundred_dict] + 'hundred'
            else:
                return words_dict[hundred_dict] + 'hundredand' + num_to_words(remainder)

def main():
    df = pd.read_csv('data/ep17.csv',header=None)
    words_dict = df.set_index(0).to_dict()[1]
    ans = sum([len(num_to_words(x)) for x in range(1,1001)])
    return ans
