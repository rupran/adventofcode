#!/usr/bin/env python3

import lib.common as lib

def gen_grid(serial_number):
    grid = [[0 for _ in range(300)] for _ in range(300)]
    for y in range(300):
        for x in range(300):
            x_1 = x + 1
            y_1 = y + 1
            rack_id = x_1 + 10
            power_level = (rack_id * y_1 + serial_number) * rack_id
            hundreds = str(power_level//100)[-1]
            grid[y][x] = int(hundreds) - 5
    return grid

def part_one(line_gen):
    serial_number = int(next(line_gen))
    grid = gen_grid(serial_number)
    max_sum = 0
    max_coord = None
    for y in range(297):
        for x in range(297):
            s = grid[y][x] + grid[y+1][x] + grid[y+2][x] + \
                grid[y][x+1] + grid[y+1][x+1] + grid[y+2][x+1] + \
                grid[y][x+2] + grid[y+1][x+2] + grid[y+2][x+2]
            if s > max_sum:
                max_coord = (x + 1, y + 1)
                max_sum = max(max_sum, s)
    return '{},{}'.format(*max_coord)

def part_two(line_gen):
    serial_number = int(next(line_gen))
    grid = gen_grid(serial_number)
    sat = [[0 for _ in range(300)] for _ in range(300)]
    sat[0][0] = grid[0][0]
    for y in range(1, 300):
        sat[y][0] = sat[y-1][0] + grid[y][0]
    for x in range(1, 300):
        sat[0][x] = sat[0][x-1] + grid[0][x]
    for x in range(1,300):
        for y in range(1, 300):
            sat[y][x] = grid[y][x] + sat[y-1][x] + sat[y][x-1] - sat[y-1][x-1]

    max_coord = None
    max_sum = 0
    max_off = -1
    for y in range(300):
        for x in range(300):
            max_sq_size = min(x, y) + 1
            for sqoff in range(max_sq_size):
                s = sat[y][x] + sat[y - sqoff][x - sqoff] - sat[y - sqoff][x] - sat[y][x - sqoff]
                if s > max_sum:
                    max_sum = s
                    # + 2 because of 0-indexing and backward offset calculation
                    max_coord = (x - sqoff + 2, y - sqoff + 2)
                    max_off = sqoff
    return '{},{},{}'.format(*max_coord, max_off)

print("A: " + str(part_one(lib.get_input(11))))
print("B: " + str(part_two(lib.get_input(11))))
