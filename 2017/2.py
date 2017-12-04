#!/usr/bin/env python3

import lib.common as lib

def part_one(line_gen):
    checksum = 0
    for line in line_gen: # multi line input
        line = [int(x) for x in line.split()]
        checksum += (max(line) - min(line))
    return checksum

def part_two(line_gen):
    checksum = 0
    for line in line_gen: # multi line input
        line = [int(x) for x in line.split()]
        found = False
        for idx, x in enumerate(line):
            if found:
                break
            for y in line[idx + 1:]:
                bigger = max(x, y)
                smaller = min(x, y)
                if bigger % smaller == 0:
                    checksum += (bigger//smaller)
                    found = True
    return checksum


print("A: " + str(part_one(lib.get_input(2))))
print("B: " + str(part_two(lib.get_input(2))))
