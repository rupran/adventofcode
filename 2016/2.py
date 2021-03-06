#!/usr/bin/env python3

import lib.common as lib

field_a = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

field_b = [['X', 'X', '1', 'X', 'X'],
           ['X', '2', '3', '4', 'X'],
           ['5', '6', '7', '8', '9'],
           ['X', 'A', 'B', 'C', 'X'],
           ['X', 'X', 'D', 'X', 'X']]

# [up/down, left/right]
pos_a = [1, 1]
pos_b = [2, 0]

def get_key(field, pos):
    return field[pos[0]][pos[1]]

def update_pos(field, pos, direction, part_b=False):
    if direction == "U":
        delta = [-1, 0]
    elif direction == "D":
        delta = [1, 0]
    elif direction == "L":
        delta = [0, -1]
    elif direction == "R":
        delta = [0, 1]

    new_pos = [pos[x] + delta[x] for x in range(len(pos))]
    retval = new_pos

    # Don't move out of bounds
    if new_pos[0] < 0 or new_pos[0] == len(field) or \
            new_pos[1] < 0 or new_pos[1] == len(field):
        retval = pos

    # And don't move into uncovered area in field_b
    elif part_b:
        if get_key(field, new_pos) == 'X':
            retval = pos

    return retval

code_a = ""
code_b = ""
for line in lib.get_input(2):
    for instr in line:
        pos_a = update_pos(field_a, pos_a, instr)
        pos_b = update_pos(field_b, pos_b, instr, part_b=True)

    code_a += str(get_key(field_a, pos_a))
    code_b += str(get_key(field_b, pos_b))

print("A: " + code_a)
print("B: " + code_b)
