# time cost = 360 µs ± 3.8 µs

def is_pandgital(x):
    digits_set = set(str(x))
    if digits_set == set(str(123456789)):
        return True
    return False

def main():
    for p in range(9487,9233,-1):
        ans = int(str(p) + str(p*2))
        if is_pandgital(ans):
            return ans
