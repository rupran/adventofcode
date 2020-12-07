#!/usr/bin/env python3

import lib.common as lib
import re

def part_one(line_gen):
    num_valid = 0
    for line in line_gen: # multi line input
        if m := re.match(r'(\d+)-(\d+) (\w): (\w+)', line):
            lower, upper, letter, string = m.groups()
            lower, upper = int(lower), int(upper)
            if lower <= string.count(letter) <= upper:
                num_valid += 1
    return num_valid

def part_two(line_gen):
    num_valid = 0
    for line in line_gen: # multi line input
        if m := re.match(r'(\d+)-(\d+) (\w): (\w+)', line):
            pos1, pos2, letter, string = m.groups()
            pos1, pos2 = int(pos1) - 1, int(pos2) - 1 # index shift
            if int(string[pos1] == letter) + int(string[pos2] == letter) == 1:
                num_valid += 1
    return num_valid

print("A: " + str(part_one(lib.get_input(2))))
print("B: " + str(part_two(lib.get_input(2))))
