#!/usr/bin/env python3

import copy
import time
import lib.common as lib

def print_field(field):
    for line in field:
        print(''.join(line))

def check_field(field, y, x, state, recurse=None):
    if y <= 0 or y >= len(field) - 1:
        return 0
    elif x <= 0 or x >= len(field[0]) - 1:
        return 0
    if field[y][x] == state:
        return 1
    if field[y][x] != '.':
        return 0
    if recurse:
        return check_field(field, y+recurse[0], x+recurse[1], state, recurse)
    return 0

def gen_deltas():
    deltas = []
    for d_y in range(-1, 2):
        for d_x in range(-1, 2):
            if (d_y, d_x) != (0, 0):
                deltas.append((d_y, d_x))
    return deltas

def sum_surrounding(field, y, x, state):
    result = 0
    for delta_y, delta_x in gen_deltas():
        result += check_field(field, y + delta_y, x + delta_x, state)
    return result

def sum_visible(field, y, x, state):
    result = 0
    for delta_y, delta_x in gen_deltas():
        result += check_field(field, y + delta_y, x + delta_x, state, (delta_y, delta_x))
    return result
    
def simulate(field, sum_function, tolerance):
    changed = True
    while changed:
        changed = False
        new_field = copy.deepcopy(field)
        for y in range(1, len(new_field) - 1):
            for x in range(1, len(new_field[y]) - 1):
                if field[y][x] == '.':
                    continue
                elif field[y][x] == 'L' and sum_function(field, y, x, '#') == 0:
                    changed = True
                    new_field[y][x] = '#'
                elif field[y][x] == '#' and sum_function(field, y, x, '#') >= tolerance:
                    changed = True
                    new_field[y][x] = 'L'
        field = new_field
    return field

def build_field(line_gen):
    field = []
    for line in line_gen: # multi line input
        field.append(list('.' + line + '.'))
    field.insert(0, list('.' * len(field[0])))
    field.append(list('.' * len(field[0])))
    return field

def count_occupied(field):
    return sum(f == '#' for row in field for f in row)

def part_one(line_gen):
    return count_occupied(simulate(build_field(line_gen), sum_surrounding, 4))

def part_two(line_gen):
    return count_occupied(simulate(build_field(line_gen), sum_visible, 5))

print("A: " + str(part_one(lib.get_input(11))))
print("B: " + str(part_two(lib.get_input(11))))
