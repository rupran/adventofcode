#!/usr/bin/env python3

import lib.common as lib

def sum_up(line, offset):
    zipped = zip(line, line[offset:] + line[:offset])
    return sum(int(x[0]) for x in zipped if x[0] == x[1])

def part_one(line_gen):
    line = next(line_gen) # one line input
    return sum_up(line, 1)

def part_two(line_gen):
    line = next(line_gen) # one line input
    return sum_up(line, len(line)//2)

print("A: " + str(part_one(lib.get_input(1))))
print("B: " + str(part_two(lib.get_input(1))))
