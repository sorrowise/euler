# time cost = 565 µs ± 11.4 µs

import re

def main():
    with open('data/ep89.txt') as f:
        romans = f.read()
    new = re.sub("DCCCC|LXXXX|VIIII|CCCC|XXXX|IIII", '**',romans)
    savings = len(romans) - len(new)
    return savings
