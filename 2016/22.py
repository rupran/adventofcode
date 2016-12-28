#!/usr/bin/env python3

import collections
import itertools
import re
import lib.common as lib

Device = collections.namedtuple('Device', 'x, y, size, used, avail')

def calc_grid_and_viable(line_gen):
    next(line_gen)  # throw away command line
    next(line_gen)  # throw away header
    device_grid = {}
    viable = set()
    # Name Size Used Avail Use%
    for line in line_gen: # multi line input
        cols = line.split()
        coords = [int(coord) for coord in
                  re.match(r"\/dev\/grid\/node-x(\d+)-y(\d+)", cols[0]).groups()]
        x, y = coords[0], coords[1]
        cur_dev = Device(x, y, *((int(val[:-1]) for val in cols[1:-1])))
        device_grid[(x, y)] = cur_dev

    for dev_a in device_grid.values():
        if dev_a.used == 0:
            continue
        for dev_b in device_grid.values():
            if dev_a == dev_b:
                continue
            if dev_a.used <= dev_b.avail:
                viable.add((dev_a, dev_b))

    return device_grid, viable

def part_one(line_gen):
    return len(calc_grid_and_viable(line_gen)[1])

def part_two(line_gen):
    device_grid, viable = calc_grid_and_viable(line_gen)
    max_x, max_y = max(device_grid.keys())
    grid_lists = [['.'] * (max_x+1) for _ in range(max_y+1)]
    grid_lists[0][max_x] = 'G'
    steps = 0
    for _, dev in device_grid.items():
        if dev.used == 0:
            grid_lists[dev.y][dev.x] = "_"
            steps += dev.y
            steps += dev.x  # Move to 0, 0 around the wall
        elif dev not in itertools.chain.from_iterable(viable):
            grid_lists[dev.y][dev.x] = "#"

    steps += max_x          # Move from 0, 0 to goal and swap empty/goal
    steps += (max_x-1)*5    # Move goal towards 0, 0, 1 tick = 5 moves
    # Note: Calculation does not work for sample input!
    for line in grid_lists:
        print(" ".join(str(x) for x in line))
    print("Look at the grid to figure it out manually")
    return steps

print("A: " + str(part_one(lib.get_input(22))))
print("B: " + str(part_two(lib.get_input(22))))
