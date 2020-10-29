# time cost = 1.58 ms ± 17.4 µs

def is_concealed_square(number):
    seq = ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']
    digits = [x for x in str(number)]
    if len(digits) == 19 and digits[0::2] == seq:
        return True
    return False

def main(n=1389026620):
    while True:
        if is_concealed_square(n**2):
            return n
        else:
            n = n - 10
