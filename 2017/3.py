#!/usr/bin/env python3

import lib.common as lib
import math

def part_one(line_gen):
    line = next(line_gen) # one line input
    target = int(line)
    sizes = int(math.sqrt(target)) + 1
    array = [[[0] for i in range(sizes)] for j in range(sizes)]
    index = [sizes//2, sizes//2]
    start_index = index[:]
    cur_shift = 1
    cur_dir_idx = 0
    cur_data = 1
    counter = 0
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    while True:
        for i in range(cur_shift):
            array[index[0]][index[1]] = cur_data
            if cur_data == target:
                return sum([abs(start_index[0] - index[0]), abs(start_index[1] - index[1])])
            cur_data += 1
            index[0] += directions[cur_dir_idx][0]
            index[1] += directions[cur_dir_idx][1]
        counter += 1
        cur_dir_idx = (cur_dir_idx + 1) % 4
        if counter == 2:
            cur_shift += 1
            counter = 0

def make_sum(data, idx):
    val = 0
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            cur_idx = [idx[0] + y, idx[1] + x]
            val += data[cur_idx[0]][cur_idx[1]]
    return val

def part_two(line_gen):
    line = next(line_gen) # one line input
    target = int(line)
    sizes = 11
    array = [[0 for i in range(sizes)] for j in range(sizes)]
    index = [sizes//2, sizes//2]
    start_index = index[:]
    array[index[0]][index[1]] = 1
    cur_shift = 1
    cur_dir_idx = 0
    counter = 0
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    while True:
        for i in range(cur_shift):
            val = make_sum(array, index)
            array[index[0]][index[1]] = val
            if val > target:
                return val
            index[0] += directions[cur_dir_idx][0]
            index[1] += directions[cur_dir_idx][1]
        counter += 1
        cur_dir_idx = (cur_dir_idx + 1) % 4
        if counter == 2:
            cur_shift += 1
            counter = 0

print("A: " + str(part_one(lib.get_input(3))))
print("B: " + str(part_two(lib.get_input(3))))
