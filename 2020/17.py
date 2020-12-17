#!/usr/bin/env python3

import copy
import lib.common as lib

def calc_active_4d(field, x, y, z, w):
    neighbours = 0
    for n_w in range(w - 1, w + 2):
        for n_z in range(z - 1, z + 2):
            for n_y in range(y - 1, y + 2):
                for n_x in range(x - 1, x + 2):
                    if (n_x, n_y, n_z, n_w) == (x, y, z, w):
                        continue
                    if get_field_4d(field, n_x, n_y, n_z, n_w) == '#':
                        neighbours += 1
    return neighbours

def get_field_4d(field, x, y, z, w):
    if x not in field:
        return '.'
    if y not in field[x]:
        return '.'
    if z not in field[x][y]:
        return '.'
    if w not in field[x][y][z]:
        return '.'
    return field[x][y][z][w]

def set_field_4d(field, x, y, z, w, state):
    if x not in field:
        field[x] = {}
    if y not in field[x]:
        field[x][y] = {}
    if z not in field[x][y]:
        field[x][y][z] = {}
    if w not in field[x][y][z]:
        field[x][y][z][w] = {}
    field[x][y][z][w] = state

def get_mins_and_maxs_4d(field):
    min_x = min(field.keys())
    max_x = max(field.keys())
    min_y = min(c for x in field.keys() for c in field[x].keys())
    max_y = max(c for x in field.keys() for c in field[x].keys())
    min_z = min(c for x in field.keys() for y in field[x].keys() for c in field[x][y].keys())
    max_z = max(c for x in field.keys() for y in field[x].keys() for c in field[x][y].keys())
    min_w = min(c for x in field.keys() for y in field[x].keys() for z in field[x][y].keys() for c in field[x][y][z].keys())
    max_w = max(c for x in field.keys() for y in field[x].keys() for z in field[x][y].keys() for c in field[x][y][z].keys())
    return min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w

def get_active_4d(field):
    min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w = get_mins_and_maxs_4d(field)
    result = 0
    for w in range(min_w, max_w + 1):
        for z in range(min_z, max_z + 1):
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    if get_field_4d(field, x, y, z, w) == '#':
                        result += 1
    return result

def simulate_4d(field, cycles=6, dimensions=3):
    for c in range(cycles):
        min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w = get_mins_and_maxs_4d(field)
        new_field = copy.deepcopy(field)
        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    # only consider w = 0 in the 3D case
                    if dimensions == 3:
                        min_w, max_w = 1, -1
                    for w in range(min_w - 1, max_w + 2):
                        n = calc_active_4d(field, x, y, z, w)
                        if get_field_4d(field, x, y, z, w) == '.' and n == 3:
                            set_field_4d(new_field, x, y, z, w, '#')
                        elif get_field_4d(field, x, y, z, w) == '#' and n not in [2, 3]:
                            set_field_4d(new_field, x, y, z, w, '.')
                        
        field = new_field

    return get_active_4d(field)

def read_field_4d(line_gen):
    field = {}
    y = 0
    for line in line_gen:
        for idx, char in enumerate(line):
            set_field_4d(field, idx, y, 0, 0, char)
        y += 1
    return field

def part_one(line_gen):
    return simulate_4d(read_field_4d(line_gen), dimensions=3)

def part_two(line_gen):
    return simulate_4d(read_field_4d(line_gen), dimensions=4)

print("A: " + str(part_one(lib.get_input(17))))
print("B: " + str(part_two(lib.get_input(17))))
