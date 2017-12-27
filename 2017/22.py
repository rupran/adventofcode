#!/usr/bin/env python3

import collections

import lib.common as lib

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def print_field(grid, pos):
    print(pos)
    for row in grid:
        print(''.join(row))

def run(line_gen, iterations, second_part=False):
    grid = collections.deque()
    for line in line_gen:
        grid.append(collections.deque(line))

    current = (len(grid[0])//2, len(grid)//2)
    if second_part:
        next_state = {'.': 'W', 'W': '#', '#': 'F', 'F': '.'}
    else:
        next_state = {'.': '#', '#': '.'}
    cur_dir_idx = 0

    infections = 0
    for _ in range(iterations):
        cur_status = grid[current[0]][current[1]]
        if cur_status == '#':
            cur_dir_idx = (cur_dir_idx + 1) % len(DIRECTIONS)
        elif cur_status == '.':
            cur_dir_idx = (cur_dir_idx - 1) % len(DIRECTIONS)
        elif cur_status == 'F':
            cur_dir_idx = (cur_dir_idx + 2) % len(DIRECTIONS)
        elif cur_status == 'W':
            pass
        grid[current[0]][current[1]] = next_state[cur_status]
        if grid[current[0]][current[1]] == '#':
            infections += 1
        next_pos = tuple((x + y for (x, y) in zip(current, DIRECTIONS[cur_dir_idx])))
        if next_pos[0] < 0:
            grid.appendleft(collections.deque('.' * len(grid[0])))
            next_pos = (0, next_pos[1])
        elif next_pos[0] == len(grid):
            grid.append(collections.deque('.' * len(grid[0])))
        elif next_pos[1] < 0:
            for row in grid:
                row.appendleft('.')
            next_pos = (next_pos[0], 0)
        elif next_pos[1] == len(grid[0]):
            for row in grid:
                row.append('.')
        current = next_pos
    return infections

def part_one(line_gen):
    return run(line_gen, 10000)
def part_two(line_gen):
    return run(line_gen, 10000000, True)

print("A: " + str(part_one(lib.get_input(22))))
print("B: " + str(part_two(lib.get_input(22))))
