import numpy as np

def import_grids():
    grids = []
    with open('data/pe096.txt') as f:
        data = f.readlines()
    for i in range(1,492,10):
        grid = [[int(x) for x in row.strip()] for row in data[i:i+9]]
        grids.append(np.array(grid))
    return grids

def is_possible(grid,n,pos):
    r,c = pos
    r0,c0 = (r//3)*3,(c//3)*3
    if n in grid[r,:]:
        return False
    elif n in grid[:,c]:
        return False
    elif n in grid[r0:r0+3,c0:c0+3]:
        return False
    else:
        return True

def iter_sudoku_solver(grid):
    rs,cs = np.where(grid==0)
    empty_cells = [(r,c) for r,c in zip(rs,cs)]
    empty_size = len(empty_cells)
    index = 0
    while index < empty_size:
        pos = empty_cells[index]
        for n in range(grid[pos]+1,10):
            if is_possible(grid,n,pos):
                grid[pos] = n
                index = index + 1
                break
        else:
            grid[pos] = 0
            index = index - 1
    return grid   

def main():
    ans = 0
    grids = import_grids()
    for grid in grids:
        g = iter_sudoku_solver(grid)
        ans += (g[0,0]*100+g[0,1]*10+g[0,2])
    return ans
