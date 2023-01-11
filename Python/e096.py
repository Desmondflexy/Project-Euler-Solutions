"""
Problem 96: Su Doku
"""
from time import time

from myfunc import array2num


def find_next_cell_to_fill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def is_valid(grid, i, j, e):
    row_ok = all([e != grid[i][x] for x in range(9)])
    if row_ok:
        column_ok = all([e != grid[x][j] for x in range(9)])
        if column_ok:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            sec_top_x, sec_top_y = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
            for x in range(sec_top_x, sec_top_x + 3):
                for y in range(sec_top_y, sec_top_y + 3):
                    if grid[x][y] == e:
                        return False
            return True
    return False


def solve_sudoku(grid, i=0, j=0):
    i, j = find_next_cell_to_fill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 10):
        if is_valid(grid, i, j, e):
            grid[i][j] = e
            if solve_sudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


def main():
    tic = time()
    book = open('p096_sudoku.txt')

    sudoku_all = []
    grid = []
    n = 1
    for line in book:
        x = line.strip()
        grid.append(x)
        n += 1
        if n % 10 == 1:
            grid = grid[1:]
            sudoku_all.append(grid)
            grid = []

    s = 0
    for puzzle in sudoku_all:
        grid = []
        for row in puzzle:
            grid.append([int(i) for i in row])

        solve_sudoku(grid)
        s += array2num(grid[0][:3])

    print(s)
    print(f'time elapsed: {time() - tic}')

main()
