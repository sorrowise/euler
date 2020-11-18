# time cost = 7.4 ms ± 81.7 µs

def min_path_sum(matrix):
    n = len(matrix)
    cost = [matrix[i][0] for i in range(n)]
    for column in range(1,n):
        cost[0] += matrix[0][column]
        for row in range(1,n):
            cost[row] = min(cost[row], cost[row-1]) + matrix[row][column]
        for row in range(n-2, -1, -1):
            cost[row] = min(cost[row], cost[row+1] + matrix[row][column])
    return min(cost)

def main():
    with open('data/pe082.txt') as f:
        matrix = [[int(x) for x in row.split(',')] for row in f.readlines()]
    return min_path_sum(matrix)
