#!/usr/bin/env python3

import lib.common as lib

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def get_next(cur, idx, prev, grid):
    nxt_y, nxt_x = tuple(y + x for (y, x) in zip(cur, DIRECTIONS[idx]))
    # Overflow in y direction
    if nxt_y < 0 or nxt_y >= len(grid):
        return None
    # Overflow in x direction
    elif nxt_x < 0 or nxt_x >= len(grid[nxt_y]):
        return None
    # Turn around
    elif (nxt_y, nxt_x) == prev:
        return None
    # Would walk into empty space
    elif grid[nxt_y][nxt_x] == ' ':
        return None
    return (nxt_y, nxt_x)

def walk(grid, second_part=False):
    cur = (0, next(idx for idx, elem in enumerate(grid[0]) if elem != ' '))
    prev = (-1, -1)
    cur_dir_idx = 0
    steps = 0
    letters = []
    while True:
        steps += 1
        cur_elem = grid[cur[0]][cur[1]]
        if cur_elem == '+':
            for idx, _ in enumerate(DIRECTIONS):
                nxt = get_next(cur, idx, prev, grid)
                if not nxt:
                    continue
                cur_dir_idx = idx
                break

        elif cur_elem.isalpha():
            letters += cur_elem

        nxt = get_next(cur, cur_dir_idx, prev, grid)
        if not nxt:
            if second_part:
                return steps
            else:
                return ''.join(letters)
        prev = cur
        cur = nxt

def read_grid(line_gen):
    return [list(line.rstrip('\n')) for line in line_gen]

def part_one(line_gen):
    return walk(read_grid(line_gen))

def part_two(line_gen):
    return walk(read_grid(line_gen), True)

print("A: " + str(part_one(lib.get_input(19, strip=False))))
print("B: " + str(part_two(lib.get_input(19, strip=False))))
