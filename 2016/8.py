#!/usr/bin/env python3

import collections
import lib.common as lib
import re

def print_field(field):
    for row in field:
        print("".join(row))

def part_one(line_gen, size_x, size_y):
    global field
    field = [[" "]* size_x for _ in range(size_y)]
    for line in line_gen:
        # Check for new rectangle
        match = re.match(r"rect (\d+)x(\d+)", line)
        if match:
            rect_x = int(match.group(1))
            rect_y = int(match.group(2))
            for y in range(0, rect_y):
                for x in range(0, rect_x):
                    field[y][x] = "#"
            continue
        # Buffer old field for rotations
        field_old = [x[:] for x in field]
        # Check for rotations
        match = re.match(r"rotate (row y|column x)=(\d+) by (\d+)", line)
        if match:
            shift = int(match.group(3))
            if match.group(1) == "column x":
                col = int(match.group(2))
                for y in range(0, size_y):
                    new_y = (y + shift) % size_y
                    field[new_y][col] = field_old[y][col]
            else:
                row = int(match.group(2))
                for x in range(0, size_x):
                    new_x = (x + shift) % size_x
                    field[row][new_x] = field_old[row][x]

    return collections.Counter(entry for row in field for entry in row)["#"]

def part_two():
    global field
    print_field(field)
    return "See image above in a wide enough terminal"

print("A: " + str(part_one(lib.get_input(8), 50, 6)))
print("B: " + str(part_two()))
