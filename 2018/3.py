#!/usr/bin/env python3

import lib.common as lib

import collections
import re

def gridfill(line_gen, part_two=False):
    grid = [[list() for _ in range(1000)]  for _ in range(1000)]
    overlapping = {}
    for line in line_gen:
        m = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', line)
        if m:
            n, x, y, width, height = (int(val) for val in m.groups())
            overlapping[n] = False
            for xi in range(x, x + width):
                for yi in range(y, y + height):
                    if grid[yi][xi]:
                        for prev in grid[yi][xi]:
                            overlapping[prev] = True
                        overlapping[n] = True
                    grid[yi][xi].append(n)
    if part_two:
        return [key for key, val in overlapping.items() if not val][0]
    else:
        return sum(sum(1 for subl in l if len(subl) > 1) for l in grid)

def part_one(line_gen):
    return gridfill(line_gen)

def part_two(line_gen):
    return gridfill(line_gen, part_two=True)

print("A: " + str(part_one(lib.get_input(3))))
print("B: " + str(part_two(lib.get_input(3))))
