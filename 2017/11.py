#!/usr/bin/env python3

import re

import lib.common as lib

POSSIBLE = {'nw': [-1, -1], 'n': [0, -2], 'ne': [1, -1],
            'se': [1, 1], 's': [0, 2], 'sw': [-1, 1]}

def get_pos(current, direction):
    return tuple(x + y for x, y in zip(current, POSSIBLE[direction]))

def get_distance_to_origin(pos):
    pos_x, pos_y = pos
    # Steps on y axis towards diagonal (1 step down/up ==2 units on axis)...
    y_dist_diag = abs(pos_y - pos_x) // 2
    # ... plus length of diagonal to origin. This also accounts for the case
    # where we're quite close to the y axis itself, as it doesn't matter if we
    # step towards the y axis diagonally first and down later or the other way
    # round (which we do here)
    total_diag_dist = y_dist_diag + abs(pos_x)
    # A shorter route might be going to the x axis and then sideways. Walk down
    # (or up, doesn't matter) to the axis and then pos_x steps sideways.
    dist_to_x_axis = abs(pos_y) // 2
    total_axis_dist = dist_to_x_axis + abs(pos_x)
    return min(total_diag_dist, total_axis_dist)

def shorten(string):
    # Ugly and slow, but worked for the first part. I'm leaving it in as a
    # warning for future readers of this code.
    while True:
        before = string[:]
        # Back to where we came from
        string = re.sub(r'ne,(.*)sw(,|$)', r'\1\2', string)
        string = re.sub(r'n,(.*)s(,|$)', r'\1\2', string)
        string = re.sub(r'nw,(.*)se(,|$)', r'\1\2', string)
        string = re.sub(r'sw,(.*)ne(,|$)', r'\1\2', string)
        string = re.sub(r's,(.*)n(,|$)', r'\1\2', string)
        string = re.sub(r'se,(.*)nw(,|$)', r'\1\2', string)

        # Compactions
        string = re.sub(r'ne,(.*)s(,|$)', r'\1se\2', string)
        string = re.sub(r'ne,(.*)nw(,|$)', r'\1n\2', string)

        string = re.sub(r'se,(.*)n(,|$)', r'\1ne\2', string)
        string = re.sub(r'se,(.*)sw(,|$)', r'\1s\2', string)

        string = re.sub(r's,(.*)ne(,|$)', r'\1se\2', string)
        string = re.sub(r's,(.*)nw(,|$)', r'\1sw\2', string)

        string = re.sub(r'n,(.*)se(,|$)', r'\1ne\2', string)
        string = re.sub(r'n,(.*)sw(,|$)', r'\1nw\2', string)

        string = re.sub(r'nw,(.*)s(,|$)', r'\1sw\2', string)
        string = re.sub(r'nw,(.*)ne(,|$)', r'\1n\2', string)

        string = re.sub(r'sw,(.*)n(,|$)', r'\1nw\2', string)
        string = re.sub(r'sw,(.*)se(,|$)', r'\1s\2', string)

        string = re.sub(r',,+', r',', string)
        if string == before:
            break

    return len([x for x in string.split(',') if x])

def walk(line_gen, second_part=False):
    directions = next(line_gen).split(',')
    all_positions = set()

    current = (0, 0)
    for direction in directions:
        current = get_pos(current, direction)
        all_positions.add(current)

    if second_part:
        return max(get_distance_to_origin(x) for x in all_positions)
    else:
        return get_distance_to_origin(current)

def part_one(line_gen):
    #return shorten(next(line_gen))
    return walk(line_gen)

def part_two(line_gen):
    return walk(line_gen, True)

print("A: " + str(part_one(lib.get_input(11))))
print("B: " + str(part_two(lib.get_input(11))))
