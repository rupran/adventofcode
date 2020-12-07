#!/usr/bin/env python3

import collections
import lib.common as lib

def get_seat(line):
    row, col = line[:7], line[7:]
    row_bin = ''.join(['0' if char == 'F' else '1' for char in row])
    row = int(row_bin, base=2)
    col_bin = ''.join(['0' if char == 'L' else '1' for char in col])
    col = int(col_bin, base=2)
    return (row, col)

def calculate_id(row, col):
    return row * 8 + col

def part_one(line_gen):
    highest_id = 0
    highest_row = 0
    for line in line_gen: # multi line input
        current_id = calculate_id(*get_seat(line))
        highest_id = max(highest_id, current_id)
    return highest_id

def part_two(line_gen):
    seats_in_row = collections.defaultdict(set)

    for line in line_gen: # multi line input
        row, col = get_seat(line)
        seats_in_row[row].add(col)
    
    max_row = max(seats_in_row.keys())
    for row, col in seats_in_row.items():
        if 0 < row < max_row and len(col) < 8:
            missing_col = set(range(8)) - col
            return calculate_id(row, missing_col.pop())

print("A: " + str(part_one(lib.get_input(5))))
print("B: " + str(part_two(lib.get_input(5))))
