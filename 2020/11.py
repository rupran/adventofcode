#!/usr/bin/env python3

import copy
import time
import lib.common as lib

def print_field(field):
    for line in field:
        print(''.join(line))

def sum_surrounding(field, y, x, state):
    result = 0
    surroundings = []
    for d_y in range(-1, 2):
        for d_x in range(-1, 2):
            if (d_y, d_x) != (0, 0):
                surroundings.append((d_y, d_x))

    for delta_y, delta_x in surroundings:
        result += int(field[y-delta_y][x-delta_x] == state)
    return result

def sum_visible(field, y, x, state):
    result = 0
    # left and up
    cur_y, cur_x = y - 1, x - 1
    while cur_y > 0 and cur_x > 0:
        if field[cur_y][cur_x] == state:
            result += 1
        if field[cur_y][cur_x] != '.':
            break
        cur_x -= 1
        cur_y -= 1
    # straight left
    cur_y, cur_x = y, x - 1
    while cur_y > 0 and cur_x > 0:
        if field[cur_y][cur_x] == state:
            result += 1
        if field[cur_y][cur_x] != '.':
            break
        cur_x -= 1
    # left and down
    cur_y, cur_x = y + 1, x - 1
    while cur_y < len(field) and cur_x > 0:
        if field[cur_y][cur_x] == state:
            result += 1
        if field[cur_y][cur_x] != '.':
            break
        cur_x -= 1
        cur_y += 1
    # straight up
    cur_y, cur_x = y - 1, x
    while cur_y > 0:
        if field[cur_y][cur_x] == state:
            result += 1
        if field[cur_y][cur_x] != '.':
            break
        cur_y -= 1
    # straight down
    cur_y, cur_x = y + 1, x
    while cur_y < len(field):
        if field[cur_y][cur_x] == state:
            result += 1
        if field[cur_y][cur_x] != '.':
            break
        cur_y += 1
    # right and up
    cur_y, cur_x = y - 1, x + 1
    while cur_y > 0 and cur_x < len(field[0]):
        if field[cur_y][cur_x] == state:
            result += 1
        if field[cur_y][cur_x] != '.':
            break
        cur_y -= 1
        cur_x += 1
    # straight right
    cur_y, cur_x = y, x + 1
    while cur_x < len(field[0]):
        if field[cur_y][cur_x] == state:
            result += 1
        if field[cur_y][cur_x] != '.':
            break
        cur_x += 1
    # right and down
    cur_y, cur_x = y + 1, x + 1
    while cur_y < len(field) and cur_x < len(field[0]):
        if field[cur_y][cur_x] == state:
            result += 1
        if field[cur_y][cur_x] != '.':
            break
        cur_y += 1
        cur_x += 1
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
