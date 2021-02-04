# timec cost = 456 ms ± 2.91 ms

from itertools import combinations

def main():
    counter = 0
    sq = {1,4,6,16,25,36,46,64,81}
    cube_number = list(range(9)) + [6]
    comb = list(combinations(cube_number,6))
    for i in comb:
        for j in comb:
            numbers = {e for x in i for y in j for e in (10*x+y,10*y+x)}
            if sq <= numbers:
                counter += 1
    return counter//2
