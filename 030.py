# time cost = 761 ms ± 19.2 ms

def main():
    power_dict = {i:i**5 for i in range(0,10)}
    res = []
    for i in range(10,6*9**5):
        sum_of_digits = sum([power_dict[int(x)] for x in str(i)])
        if i == sum_of_digits:
            res.append(i)
    return sum(res)
