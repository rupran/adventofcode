#!/usr/bin/env python3

import lib.common as lib

def make_grid(line_gen):
    grid = []
    for line in line_gen: # multi line input
        grid.append(line)
    return grid

def walk_grid(grid, step_right, step_down):
    width = len(grid[0])
    height = len(grid)
    pos_x, pos_y, trees = 0, 0, 0

    while True:
        pos_x = (pos_x + step_right) % width
        pos_y = (pos_y + step_down)
        if pos_y >= height:
            break
        if grid[pos_y][pos_x] == '#':
            trees += 1
    return trees

def part_one(line_gen):
    return walk_grid(make_grid(line_gen), 3, 1)

def part_two(line_gen):
    grid = make_grid(line_gen)
    result = 1
    for step_right, step_down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        result *= walk_grid(grid, step_right, step_down)
    return result

print("A: " + str(part_one(lib.get_input(3))))
print("B: " + str(part_two(lib.get_input(3))))
