#!/usr/bin/python3
'''0-island_perimeter'''


def island_perimeter(grid):
    '''island perimeter'''
    count = 0

    for i in range(1, len(grid)-1):
        for j in len(1, len(grid[0]) - 1):
            if grid[i][j] == 1:
                count += 4
            if grid[i-1][j] == 1:
                count -= 1
            if grid[i+1][j] == 1:
                count -= 1
            if grid[i][j-1] == 1:
                count -= 1
            if grid[i][j+1] == 1:
                count -= 1
    return count
