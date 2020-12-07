#!/usr/bin/env python3

import lib.common as lib

def part_one(line_gen):
    total_count = 0
    current_set = set()
    for line in line_gen:
        if not line:
            total_count += len(current_set)
            current_set = set()
        else:
            current_set |= set(char for char in line)
    total_count += len(current_set)
    return total_count

def part_two(line_gen):
    total_count = 0
    current_set = set()
    new_set = True
    for line in line_gen:
        if new_set:
            current_set.update(char for char in line)
            new_set = False
        if not line:
            total_count += len(current_set)
            current_set = set()
            new_set = True
        else:
            current_set &= set(char for char in line)
    total_count += len(current_set)
    return total_count

print("A: " + str(part_one(lib.get_input(6))))
print("B: " + str(part_two(lib.get_input(6))))
