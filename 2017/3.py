#!/usr/bin/env python3

import lib.common as lib
import math

cur_data = 1

def walk_grid(array_size, val_func, target_func, target):
    array = [[0 for i in range(array_size)] for j in range(array_size)]
    index = (array_size//2, array_size//2)
    array[index[0]][index[1]] = 1
    cur_walk_len = 1
    direction_idx = 0
    counter = 0
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    while True:
        for _ in range(cur_walk_len):
            value = val_func(array, index)
            if target_func(value, target):
                return (index, value)
            array[index[0]][index[1]] = value
            index = tuple(x + y for x, y in zip(index, directions[direction_idx]))
        counter += 1
        direction_idx = (direction_idx + 1) % 4
        if counter % 2 == 0:
            cur_walk_len += 1

def part_one_value(data, index):
    global cur_data
    retval = cur_data
    cur_data += 1
    return retval

def part_one(line_gen):
    target = int(next(line_gen))
    size = int(math.sqrt(target)) + 1
    index, _ = walk_grid(size, part_one_value, lambda x, y: x == y, target)
    return sum(abs(x - y) for x, y in zip((size//2, size//2), index))

def part_two_value(data, idx):
    val = 0
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            cur_idx = (idx[0] + y, idx[1] + x)
            val += data[cur_idx[0]][cur_idx[1]]
    return val

def part_two(line_gen):
    target = int(next(line_gen))
    _, value = walk_grid(11, part_two_value, lambda x, y: x > y, target)
    return value

print("A: " + str(part_one(lib.get_input(3))))
print("B: " + str(part_two(lib.get_input(3))))
