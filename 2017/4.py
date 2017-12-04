#!/usr/bin/env python3

import lib.common as lib

def part_one(line_gen):
    valid = 0
    for line in line_gen: # multi line input
        line = line.split()
        valid += int(len(set(line)) == len(line))
    return valid

def part_two(line_gen):
    valid = 0
    for line in line_gen: # multi line input
        line = line.split()
        sorted_words = [''.join(sorted(x)) for x in line]
        valid += int(len(set(sorted_words)) == len(sorted_words))
    return valid

print("A: " + str(part_one(lib.get_input(4))))
print("B: " + str(part_two(lib.get_input(4))))
